n = int(input())
a = [int(x) for x in input().split()]
x = 0
for i in range(0, n):
    if a[i] % 2 == 1:
        x = x + 1
cnt = n - x
if cnt > x:
    cnt = x
x = x - (n - x)
if x > 0:
    cnt += int(x / 3)
print(cnt)
