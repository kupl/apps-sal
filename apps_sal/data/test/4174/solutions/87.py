
n,x = list(map(int, input().split()))
a = list(map(int, input().split()))
cnt = 1
total = 0

for i in range(n):
    total += a[i]
    if total <= x:
        cnt += 1
print(cnt)

