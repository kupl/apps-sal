n, k = list(map(int, input().split()))

l = k - 1
r = n - k

print(1 + n + 2 * min(l, r) + max(l, r) + n)

