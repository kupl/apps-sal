import sys
input = sys.stdin.readline
(n, h, m) = map(int, input().split())
arr = []
for i in range(n):
    arr.append(h)
for i in range(m):
    (l, r, x) = map(int, input().split())
    for j in range(l - 1, r):
        arr[j] = min(arr[j], x)
count = 0
for i in range(n):
    count += arr[i] ** 2
print(count)
