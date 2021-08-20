(n, m) = list(map(int, input().split()))
g = [input() for i in range(n)]
print(sum([1 for i in range(n) for j in range(m) if g[i][j] == '.' and (not (any([g[i][k] == 'S' for k in range(m)]) and any([g[k][j] == 'S' for k in range(n)])))]))
