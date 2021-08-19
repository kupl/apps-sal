N = int(input())
K = int(input())
x = list(map(int, input().split()))
sum = 0
for i in range(N):
    dist = min(x[i], abs(x[i] - K))
    sum += dist
print(sum * 2)
