(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
diff = []
if n == 1:
    print(0)
else:
    for i in range(n - 1):
        diff.append(a[i + 1] - a[i])
    diff.sort(reverse=True)
    ans = a[-1] - a[0]
    for i in range(min(k - 1, len(diff))):
        ans -= diff[i]
    print(ans)
