(n, m) = map(int, input().split())
r = [list(map(int, input().split())) for j in range(m)]
v = min((ri[1] - ri[0] + 1 for ri in r))
print(v, ' '.join((str(i % v) for i in range(n))), sep='\n')
