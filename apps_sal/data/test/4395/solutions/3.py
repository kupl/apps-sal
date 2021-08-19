n = int(input())
s = input().strip()
(best, ans) = (n, None)
for p in ('RGB', 'RBG', 'GRB', 'GBR', 'BRG', 'BGR'):
    t = p * ((n + 2) // 3)
    c = sum((x != y for (x, y) in zip(s, t)))
    if c < best:
        best = c
        ans = t[:n]
print(best, ans, sep='\n')
