n = int(input())
l = list(map(int, input().split()))
s = [0] * n
a = [0] * n
s[-1] = l[-1]
for i in range(1, n):
    if l[n - i - 1] <= s[n - i]: a[n - i - 1] = s[n - i] - l[n - i - 1] + 1
    s[n - i - 1] = max(l[n - i - 1], s[n - i])
print(' '.join(map(str, a)))
