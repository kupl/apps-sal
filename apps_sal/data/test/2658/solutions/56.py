N, K = map(int, input().split())
A = list(map(int, input().split()))

count = [-1] * (N + 1)
pos = 1
num = 0
while count[pos] == -1:
    count[pos] = num
    pos = A[pos - 1]
    num += 1

loop = max(count) - count[pos] + 1

if num > K:
    print(count.index(K))
elif loop == 1 and num <= K:
    print(count.index(max(count)))
else:
    start = num - loop
    ans = (K - num) % loop
    print(count.index(start + ans))
