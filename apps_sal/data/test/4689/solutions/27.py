(k, n) = map(int, input().split())
a = list(map(int, input().split()))
longest = k - a[-1] + a[0]
for i in range(len(a) - 1):
    longest = max(longest, a[i + 1] - a[i])
print(k - longest)
