N = int(input())
t = list(map(int, input().split()))
v = list(map(int, input().split()))
u = [0]
for vi, ti in zip(v, t):
    u[-1] = min(u[-1], vi)
    u += [vi] * (ti * 2)

u[-1] = 0
U = u.copy()
T = len(u)
for i in range(1, T):
    u[i] = min(u[i], u[i - 1] + 0.5)

for i in range(T - 2, -1, -1):
    u[i] = min(u[i], u[i + 1] + 0.5)

ans = 0
for i in range(1, T):
    ans += (u[i - 1] + u[i]) * 0.25

print(ans)
