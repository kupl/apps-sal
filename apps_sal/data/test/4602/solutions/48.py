N = int(input())
K = int(input())
x = list(map(int, input().split()))
calc = 0
for i in range(N):
    calc += min(x[i], abs(K - x[i])) * 2
print(calc)
