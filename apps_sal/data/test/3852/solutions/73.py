n = int(input())
a = list(map(int, input().split()))

mx_i = 0
for i, e in enumerate(a):
    if abs(e) > abs(a[mx_i]):
        mx_i = i

ans = []
for i in range(n):
    if i == mx_i:
        continue
    a[i] += a[mx_i]
    ans.append([mx_i + 1, i + 1])

if a[mx_i] > 0:
    for i in range(n - 1):
        if a[i] > a[i+1]:
            a[i+1] += a[i]
            ans.append([i + 1, i + 2])

else:
    for i in range(n - 1, 0, -1):
        if a[i] < a[i-1]:
            a[i-1] += a[i]
            ans.append([i + 1, i])

print((len(ans)))
for row in ans:
    print((*row))

