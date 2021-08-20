(n, t) = map(int, input().split())
a = list(map(int, input().split()))
j = ans = sumition = 0
for i in range(n):
    sumition += a[i]
    while sumition > t:
        sumition -= a[j]
        j += 1
    ans = max(ans, i - j + 1)
print(ans)
