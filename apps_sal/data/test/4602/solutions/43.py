N = int(input())
K = int(input())
x = list(map(int, input().split()))
sum = 0
for i in range(N):
    if x[i] >= K - x[i]:
        sum += 2 * (K - x[i])
    else:
        sum += 2 * x[i]
print(sum)
