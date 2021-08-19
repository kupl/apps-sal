input()
(k, m) = [int(i) for i in input().split(' ')]
a = [int(i) for i in input().split(' ')]
b = [int(i) for i in input().split(' ')]
print('YES' if a[k - 1] < b[-m] else 'NO')
