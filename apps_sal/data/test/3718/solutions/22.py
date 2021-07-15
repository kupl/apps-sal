n = int(input())
a = [int(x) for x in input().split()]
for i in range(n):
    for j in range(n):
        for k in range(n):
            if a[i] + 1 == a[j] and a[j] + 1 == a[k]:
                print('YES')
                return
print('NO')


