(w, m) = list(map(int, input().split()))
for u in (w ** (100 - i) for i in range(101)):
    m = min(m, abs(m - u))
print('YES' if m == 0 else 'NO')
