(n, d) = map(int, input().split())
a = sorted(list(map(int, input().split())))
ans = n - 1
for i in range(len(a)):
    j = i
    while j < len(a) and a[j] - a[i] <= d:
        j += 1
    ans = min(ans, n - (j - i))
print(ans)
