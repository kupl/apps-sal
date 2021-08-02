n = int(input())
a = [-1] + list(map(int, input().split()))
now = 0
for i in range(1, n + 1):
    if now + 1 == a[i]:
        now += 1
if now == 0:
    print(-1)
else:
    print(n - now)
