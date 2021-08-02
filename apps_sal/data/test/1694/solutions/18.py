n, m, s, f = list(map(int, input().split()))
if s < f:
    d = 1
    c = 'R'
else:
    d = -1
    c = 'L'
res = ''
i, j = 1, s
t, l, r = list(map(int, input().split()))
k = 1
while j != f:
    if i > t and k < m:
        t, l, r = list(map(int, input().split()))
        k += 1
    if i == t and (l <= j <= r or l <= j + d <= r):
        res += 'X'
    else:
        res += c
        j += d
    i += 1
print(res)
