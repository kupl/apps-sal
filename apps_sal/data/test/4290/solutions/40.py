from scipy.special import comb
n,m=map(int, input().split())
print(comb(n,2,exact=True)+comb(m,2,exact=True))
