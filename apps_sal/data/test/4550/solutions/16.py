a = list(map(int, input().split()))
a = sorted(a)
print('Yes' if a[0] + a[1] == a[2] else 'No')
