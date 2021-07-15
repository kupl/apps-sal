#bはKより真に大きい、N以下
#aはK以上

N, K = list(map(int, input().split()))

count = 0
for b in range(K+1, N+1):
    x = N // b
    y = N % b
    count += x * (b-K)
    count += max(0, (y-max(1,K)+1))

print(count)

