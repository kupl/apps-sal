n, k = map(int, input().split())
s = list(map(int, input().split()))

p1 = []
p2 = []

if n <= k:
    print(max(s))
else:
    for i in range(n - k):
        p1.append(s[i] + s[2 * (n - k) - i - 1])
        p2.append(s[2 * i] + s[2 * i + 1])

    for i in range(n - k + 1, n):
        p1.append(s[i])
        p2.append(s[i])

    print(min(max(p1), max(p2)))
