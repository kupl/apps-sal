(n, l) = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
ans = 2 * max(a[0], l - a[len(a) - 1])
for i in range(0, len(a) - 1):
    ans = max(ans, a[i + 1] - a[i])
print(ans / 2)
