n = int(input())
rocks = list(map(int, input().split()))
sortrocks = [0] * n
for i in range(n):
    sortrocks[i] = rocks[i]
sortrocks.sort()
v = [0] * (n + 1)
v[1] = rocks[0]
u = [0] * (n + 1)
u[1] = sortrocks[0]
for i in range(2, n + 1):
    v[i] = v[i - 1] + rocks[i - 1]
    u[i] = u[i - 1] + sortrocks[i - 1]
m = int(input())
for i in range(m):
    (type, l, r) = list(map(int, input().split()))
    l -= 1
    if type == 1:
        print(v[r] - v[l])
    else:
        print(u[r] - u[l])
