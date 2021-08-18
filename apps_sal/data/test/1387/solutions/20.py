c = input().split()
n = int(c[0])
t = int(c[1])
c = input().split()

for i in range(n - 1):
    c[i] = int(c[i])

a = 1
while (a < n) and (a < t):
    a += c[a - 1]

if a == t:
    print('YES')
else:
    print('NO')
