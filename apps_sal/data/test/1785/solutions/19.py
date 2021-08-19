(n, s) = (int(input()), input())
c = sorted((s.count(b) for b in 'ACGT'))
print(c.count(c[-1]) ** n % (10 ** 9 + 7))
