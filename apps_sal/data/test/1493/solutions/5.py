(n, m) = map(int, input().split())
for i in range(n):
    (s, t) = (input(), '')
    for j in range(m):
        t += s[j] if s[j] == '-' else 'BW'[(i + j) % 2]
    print(t)
