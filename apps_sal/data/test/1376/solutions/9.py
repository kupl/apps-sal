n = int(input())
d1 = {}
d2 = {}
a = list(map(int, input().split()))
for i in range(2 * n):
    if a[i] not in d1:
        d1[a[i]] = i
    else:
        d2[a[i]] = i
ans = abs(d1[1])
ans += abs(d2[1])
for i in range(2, n + 1):
    ans += abs(d1[i] - d1[i - 1])
    ans += abs(d2[i] - d2[i - 1])
print(ans)
