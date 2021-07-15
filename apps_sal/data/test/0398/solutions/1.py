read = lambda: map(int, input().split())
n = int(input())
a = sorted(read())
for i in range(2, n):
    if a[i - 2] + a[i - 1] > a[i]:
        print('YES')
        break
else:
    print('NO')
