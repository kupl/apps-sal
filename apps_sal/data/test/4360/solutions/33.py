N = int(input())
A = list(map(int, input().split()))
asum = 0
for i in range(N):
    asum += 1 / A[i]
print(1 / asum)
