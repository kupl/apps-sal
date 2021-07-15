n = int(input())
l = list(map(int, input().split()))
r = list(map(int, input().split()))
fl = 0
m = n
s = list(range(n))
for i in range(n):
    s[i] = m - (l[i] + r[i])
    if fl != 1 and s[i] == m:
        fl = 1
for i in range(n):
    ll = 0;
    for j in range(i):
        if s[j] > s[i]:
            ll += 1
    rr = 0
    for j in range(i + 1, n):
        if s[j] > s[i]:
            rr += 1
    if l[i] != ll or rr != r[i]:
        fl = 0
        break

if fl == 1 and l[0] == 0 and r[n - 1] == 0:
    print('YES')
    print(*s)
else:
    print('NO')



