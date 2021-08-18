n, k = map(int, input().split())
a = list(map(int, input().split()))
p = [-1] * (n + 1)
s = [-1] * (n + 1)
for i in range(k):
    if p[a[i]] == -1:
        p[a[i]] = i
for i in range(k - 1, -1, -1):
    if s[a[i]] == -1:
        s[a[i]] = i
count = 0
for i in range(1, n + 1):
    if p[i] == -1:
        if i == 1 or i == n:
            count += 2
            continue
        count += 3
    else:
        if i != n and (s[i + 1] == -1 or s[i + 1] < p[i]):
            count += 1
        if i != 1 and (s[i - 1] == -1 or s[i - 1] < p[i]):
            count += 1
print(count)
