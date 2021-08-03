n = int(input())
arr = []
for i in range(n):
    h, m = map(int, input().split(':'))
    cur = h * 60 + m
    arr.append(cur)
arr.sort()
arr.append(24 * 60 + arr[0])
maxx = 0
for i in range(1, len(arr)):
    maxx = max(maxx, arr[i] - arr[i - 1] - 1)
m = maxx % 60
h = maxx // 60
if (h < 10):
    print(0, end='')
print(h, ':', sep='', end='')
if (m < 10):
    print(0, end='')
print(m)
