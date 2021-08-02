n = int(input())
a = sorted(map(int, input().split()))
print('YES' if a[n] > a[n - 1] else 'NO')
