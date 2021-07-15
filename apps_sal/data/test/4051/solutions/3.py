n = int(input())

a = list(map(int, input().split()))
for i in range(n - 1):
    if abs(a[i] - a[i + 1]) >= 2:
        print('NO')
        return
print('YES')
