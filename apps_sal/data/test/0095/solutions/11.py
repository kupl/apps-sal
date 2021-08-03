n = int(input())
m = [int(i) for i in input().split()]
s = 0
f = 0
for j in range(n - 1):
    if m[j] < m[j + 1]:
        s2 = 0
    elif m[j] == m[j + 1]:
        s2 = 1
    else:
        s2 = 2
    if s2 > s:
        s = s2
    elif s2 < s:
        f = 1
if f == 0:
    print('YES')
else:
    print('NO')
