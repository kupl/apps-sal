(n, k) = list(map(int, input().split()))
(a, b, s, d) = input().split()
if n < 5 or k < n + 1:
    print(-1)
else:
    l = list(set(map(str, list(range(1, n + 1)))) - {a, b, s, d})
    print(' '.join([a, s] + l + [d, b] + [s, a] + l + [b, d]))
