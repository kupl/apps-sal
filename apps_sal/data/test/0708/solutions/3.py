(n, k) = list(map(int, input().split()))
(a, b, c, d) = input().split()
if n < 5 or k < n + 1:
    print(-1)
else:
    l = list(set(map(str, list(range(1, n + 1)))) - {a, b, c, d})
    print(' '.join([a, c] + l + [d, b] + [c, a] + l + [b, d]))
