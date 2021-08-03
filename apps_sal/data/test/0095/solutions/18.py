n = int(input())

a = list(map(int, input().split()))

i = 0
while i < n - 1 and a[i] < a[i + 1]:
    i += 1

while i < n - 1 and a[i] == a[i + 1]:
    i += 1

while i < n - 1 and a[i] > a[i + 1]:
    i += 1

if i == n - 1:
    print('YES')
else:
    print('NO')
