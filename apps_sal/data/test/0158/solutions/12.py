n = int(input())
l = [int(i) for i in input().split()]
l.sort()
if l[n] > l[n - 1]:
    print('YES')
else:
    print('NO')
