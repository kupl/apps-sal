n = int(input())
a = sorted(map(int, input().split(' ')))
f = False
for i in range(n - 2):
    if a[i] + a[i + 1] > a[i + 2]:
        f = True
print('YES' if f else 'NO')
