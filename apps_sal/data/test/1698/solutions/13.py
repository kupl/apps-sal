[n, k], a, i, ans, t = list(map(int, input().split())), sorted(map(int, input().split())), 0, 0, 1
while i < len(a):
    ans += ((n + k - 1) // k * 2 - 1) * (a[i] - t)
    t = a[i]
    while i < len(a) and a[i] == t:
        i += 1
        n -= 1
print(ans + t - 1)

