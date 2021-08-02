n = int(input())
x = list(map(int, input().split()))
c = 0
tot = 0
for i in range(n - 1):
    if x[i] > x[i + 1]:
        c = x[i] - x[i + 1]
        tot = tot + c
        x[i + 1] = x[i + 1] + c
print(tot)
