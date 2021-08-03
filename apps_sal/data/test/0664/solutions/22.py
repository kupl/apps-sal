n = list(map(int, input().split()))[0]
a = list(map(int, input().split()))

flag = 0
for i in range(1, n):
    if a[i] < a[i - 1]:
        flag = i

ans = True
for i in range(flag + 1, n - 1):
    if a[i + 1] < a[i]:
        ans = False

for i in range(flag - 1):
    if a[i + 1] < a[i]:
        ans = False

if flag != 0 and a[n - 1] > a[0]:
    ans = False

if not ans:
    print("-1")
else:
    print((n - flag) % n)
