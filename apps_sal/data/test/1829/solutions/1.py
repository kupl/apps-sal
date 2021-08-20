q = input().split()
n = int(q[0])
m = int(q[1])
c = 0
s = ['' for i in range(n)]
t = ['' for i in range(m)]
for i in range(n):
    s[i] = input()
for i in range(m):
    t[i] = input()
if n > m:
    print('YES')
elif n < m:
    print('NO')
else:
    for a in s:
        if a in t:
            c += 1
    if c % 2 == 1:
        print('YES')
    else:
        print('NO')
