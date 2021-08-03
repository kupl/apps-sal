
n = int(input())
a = input().split(' ')
a = [int(a) for a in a]
b = [-1 for b in range(0, n)]

now = 0

while now < n:
    start = now
    while (now < n - 1) and (a[now] < a[now + 1]):
        now += 1
    while start <= now:
        b[start] = now
        start += 1

    now += 1
    start = now

ans = 0

for i in range(0, n):
    if b[i] == n - 1:
        ans = max(ans, b[i] - i + 1)
    elif b[i] == n - 2:
        ans = max(ans, b[i] - i + 2)
    elif a[b[i] + 2] - a[b[i]] > 1:
        ans = max(ans, b[b[i] + 2] - i + 1)
    else:
        ans = max(ans, b[i] - i + 2)
        if b[i] == 0 or a[b[i] + 1] - a[b[i] - 1] > 1:
            ans = max(ans, b[b[i] + 1] - i + 1)
    if i != 0 and n != 1:
        ans = max(ans, b[i] - i + 2)
print(ans)
