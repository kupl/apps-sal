def R():
    return map(int, input().split())


(n, m) = R()
d = sorted(R()) if m > 0 else [0]
print('NO' if d[0] == 1 or d[-1] == n or any((d[i + 2] - d[i] < 3 for i in range(m - 2))) else 'YES')
