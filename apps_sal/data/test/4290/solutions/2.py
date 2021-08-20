from scipy.special import comb
(n, m) = map(int, input().split())
print(int(comb(n, 2) + comb(m, 2)))
