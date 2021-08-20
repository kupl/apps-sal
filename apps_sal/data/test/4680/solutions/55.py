a = list(map(int, input().split()))
a.sort()
print('YES' if a[0] == 5 and a[1] == 5 and (a[2] == 7) else 'NO')
