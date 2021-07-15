n = int(input())
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = list(map(int, input().split()))
p = x[0] + y[0] & 1
for i in range(n):
    if x[i] + y[i] & 1 != p:
        print((-1))
        return
d = ([1] if p == 0 else []) + [2 ** i for i in range(39)]
print((len(d)))
print((*d))

dx = [1,0,-1,0]
dy = [0,1,0,-1]
ch = 'LDRU'

for i in range(n):
    s, t = x[i], y[i]
    ans = []
    now = 2 ** 38
    for _ in range(len(d)):
        min_cur = 10 ** 18
        for i in range(4):
            ts, tt = s + dx[i] * now, t + dy[i] * now
            tm = abs(ts) + abs(tt)
            if tm < min_cur:
                ns, nt = ts, tt
                nc = ch[i]
                min_cur = tm
        s, t = ns, nt
        ans.append(nc)
        now = now // 2 if now > 1 else 1
    print((''.join(reversed(ans))))

