n, l = map(int, input().split())
ans = False
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(l):
    c = 1
    p = b[:]
    for j in range(n):
        p[j] = (b[j] + i) % l
    p.sort()
    for j in range(n):
        if a[j] != p[j]:
            c = 0
            break
    if c:
        print('YES')
        break
else:
    print('NO')
