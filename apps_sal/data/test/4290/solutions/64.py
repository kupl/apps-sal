from scipy.special import comb
(n, m) = list(map(int, input().split()))
if n <= 1:
    a = 0
else:
    a = comb(n, 2, exact='true')
if m <= 1:
    b = 0
else:
    b = comb(m, 2, exact='true')
print(a + b)
