s = input()
N = len(s)
d1 = [0] * N
d2 = [0] * N
for i in range(N - 1):
    if s[i:i + 2] == 'vv':
        d1[i] += 1
for i in range(1, N):
    d1[i] += d1[i - 1]
for i in range(N - 1, 0, -1):
    if s[i] == 'v' and s[i - 1] == 'v':
        d2[i] = 1
for i in range(N - 2, -1, -1):
    d2[i] += d2[i + 1]
ans = 0
for i in range(N):
    if s[i] == 'o':
        ans += d1[i] * d2[i]
print(ans)
