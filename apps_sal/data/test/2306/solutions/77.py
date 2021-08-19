N = int(input())
T = list(map(int, input().split()))
V = list(map(int, input().split()))
max_t = sum(T)
vl = [0] * (max_t + 1)
vr = [0] * (max_t + 1)
vm = [0] * (max_t + 1)
t = 0
for (s, u) in zip(T, V):
    for i in range(t, t + s):
        vm[t] = u
        t += 1
t = 1
for (s, u) in zip(T, V):
    for i in range(t, t + s):
        vl[t] = min(u, vl[t - 1] + 1)
        t += 1
t = max_t
for (s, u) in zip(T[::-1], V[::-1]):
    for i in range(t - s, t)[::-1]:
        vr[t - 1] = min(u, vr[t] + 1)
        t -= 1
v = [min(vl[i], vr[i]) for i in range(max_t + 1)]
ans = 0
for i in range(max_t):
    ans += (v[i] + v[i + 1]) / 2
    if v[i] == v[i + 1] and v[i] != vm[i]:
        ans += 0.25
print('{:.10f}'.format(ans))
