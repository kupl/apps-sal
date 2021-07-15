n = int(input())
t = list(map(int, input().split()))
m = int(input())
a = []
for _ in range(m):
    p, x = map(int, input().split())
    u = t[:]
    u[p - 1] = x
    a.append(sum(u))
for i in range(m):
    print(a[i])
