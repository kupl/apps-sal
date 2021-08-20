(N, T) = map(int, input().split())
c = [0 for i in range(N)]
t = [0 for i in range(N)]
for i in range(N):
    (c[i], t[i]) = map(int, input().split())
flag = False
ok = []
for i in range(N):
    if t[i] <= T:
        ok.append(t.index(t[i]))
        flag = True
ans = 1001
for i in ok:
    if ans > c[i]:
        ans = c[i]
if flag:
    print(ans)
else:
    print('TLE')
