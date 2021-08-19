n = int(input())
a = [0] + [int(i) for i in input().split()] + [1001]
ans = 0
for j in range(1, n + 1):
    i = j
    f = 0
    while i < n + 1 and a[i] == a[i - 1] + 1 and (a[i] == a[i + 1] - 1):
        f += 1
        i += 1
    ans = max(ans, f)
print(ans)
