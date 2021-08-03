n, s, t = list(map(int, input().split()))
p = [0]
p.extend(list(map(int, input().split())))
f = [0] * (n + 1)

f[s] = 1
cnt = 0
while s != t:
    s = p[s]
    cnt += 1
    if f[s] == 1:
        break

if s == t:
    print(cnt)
else:
    print(-1)
