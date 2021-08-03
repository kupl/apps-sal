N = int(input())
a = list(map(int, input().split()))

calc = 0

for i in range(N):
    calc += a[i] - 1

print(calc)
