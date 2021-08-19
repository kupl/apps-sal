(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
for i in range(m):
    for j in range(b[i]):
        c.append(i + 1)
flag = 1
for i in range(n - len(c) + 1):
    temp = a[i:i + len(c)]
    if sorted(temp) == sorted(c):
        print('YES')
        flag = 0
        break
if flag:
    print('NO')
