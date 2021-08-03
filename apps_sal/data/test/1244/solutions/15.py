n = int(input())
a = list(map(int, input().split()))

b = {}
for i in range(n):
    if a[i] in b:
        b[a[i]] += 1
    else:
        b[a[i]] = 1

if max(b.values()) <= (n + 1) // 2:
    print('YES')
else:
    print('NO')
