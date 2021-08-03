n, t = list(map(int, input().split()))
a = list(map(int, input().split()))
current = 1
while current < t:
    current = current + a[current - 1]

if current == t:
    print('YES')
else:
    print('NO')
