h1, m1 = map(int, input().split(':'))
h2, m2 = map(int, input().split(':'))
diff = h1 * 60 + m1 + ((h2 * 60 + m2) - (h1 * 60 + m1)) // 2
hres = diff // 60
mres = diff % 60
print(str(hres).zfill(2), str(mres).zfill(2), sep=':')
