n = int(input())
a = list(map(int, input().split()))
if n % 2 == 0:
    for i in range(n):
        if i < int(n / 2):
            print(a[n - 2 * i - 1], '', end='')
        else:
            print(a[2 * i - n], '', end='')
else:
    for i in range(n):
        if i <= n // 2:
            print(a[n - 2 * i - 1], '', end='')
        else:
            print(a[2 * i - n], '', end='')
print()
