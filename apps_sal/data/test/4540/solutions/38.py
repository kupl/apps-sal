n = int(input())
a = [0] + list(map(int, input().split())) + [0]
ans = 0
for i in range(n + 1):
    ans += abs(a[i] - a[i + 1])
for i in range(1, n + 1):
    if a[i - 1] <= a[i] <= a[i + 1] or a[i - 1] >= a[i] >= a[i + 1]:
        print(ans)
    else:
        print(ans - 2 * min(abs(a[i - 1] - a[i]), abs(a[i] - a[i + 1])))
