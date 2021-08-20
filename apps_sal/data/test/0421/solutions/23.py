n = int(input())
a = []
for i in range(n):
    (x, y) = list(map(int, input().split()))
    a.append((y, x))
a.sort()
cnt = 0
cur = -10
i = 0
while i < n:
    if cur < a[i][1]:
        cur = a[i][0]
        cnt += 1
    i += 1
print(cnt)
