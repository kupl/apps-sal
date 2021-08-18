n = int(input())
p = list(map(int, input().split()))
for i in range(n):
    for j in range(n):
        a = p[:]
        a[i], a[j] = a[j], a[i]
        if a == sorted(a):
            print('YES')
            return
print('NO')
