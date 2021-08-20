s = input().split(' ')
p = int(s[0])
q = int(s[1])
s = input()
n = int(s)
s = input().split(' ')
ok = True
for i in range(n):
    x = int(s[i])
    p = p - q * x
    if ok == False:
        continue
    if p == 0 and i != n - 1:
        ok = False
    elif p < 0:
        ok = False
    t = p
    p = q
    q = t
if ok and (p == 0 or q == 0):
    print('YES')
else:
    print('NO')
