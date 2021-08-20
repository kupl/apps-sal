(n, tab, changes) = (int(input()), str(input()), 1)
for i in range(1, n):
    changes += 1 if tab[i] != tab[i - 1] else 0
print(min(changes + 2, n))
