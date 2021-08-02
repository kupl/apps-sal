n = int(input())
u = list(map(int, input().split()))
u.sort()
value = (u[0] + u[1]) / 2
for i in range(2, n):
    value = (value + u[i]) / 2
print(value)
