a = sorted(list(map(int, input().split())))
print('Yes' if sum(a[:3]) == a[3] or a[0] + a[3] == a[1] + a[2] else 'No')
