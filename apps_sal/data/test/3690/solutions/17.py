(H, M, S, T1, T2) = list(map(int, input().split()))
h = H % 12 * 30 + M % 60 * 0.5 + S % 60 * (1 / 120)
m = M % 60 * 6 + S % 60 * 0.1
s = S % 60 * 6
t1 = T1 % 12 * 30
t2 = T2 % 12 * 30
(h, m, s) = sorted([h, m, s])
flag = False
if h < t1 < m and h < t2 < m:
    flag = True
elif m < t1 < s and m < t2 < s:
    flag = True
elif (s < t1 <= 360 or 0 <= t1 < h) and (s < t2 <= 360 or 0 <= t2 < h):
    flag = True
if flag:
    print('YES')
else:
    print('NO')
