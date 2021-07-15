R = lambda: map(int, input().split())
n, m = R()
d = sorted(R()) if m > 0 else []
print("YES" if len(d) == 0 or d[0] != 1 and d[m - 1] != n and all(d[i + 2] - d[i] > 2 for i in range(m - 2)) else "NO")
