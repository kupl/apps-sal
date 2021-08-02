def bet(x):
    return t1 <= x <= t2 or t2 <= x + 3600 * 12 <= t1 or t2 <= x <= t1


def read(): return map(int, input().split())


h, m, s, t1, t2 = read()
h %= 12
t1 %= 12
t2 %= 12
N = 12 * 3600 + 10
nt = [0] * N
k1 = h * 3600 + 1
k2 = m * 720 + 1
k3 = s * 720
t1 *= 3600
t2 *= 3600
if t1 > t2:
    t1, t2 = t2, t1
ans = 'NO'
flag = 1
if bet(k1) or bet(k2) or bet(k3):
    flag = 0
if flag:
    ans = 'YES'
flag = 1
t1 += 12 * 3600
if bet(k1) or bet(k2) or bet(k3):
    flag = 0
if flag:
    ans = 'YES'
print(ans)
