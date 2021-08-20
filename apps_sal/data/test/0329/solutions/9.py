st = input()
a = {'n': 0, 'i': 0, 'e': 0, 't': 0}
for c in st:
    if c in a:
        a[c] += 1
print(max(min([(a['n'] - 1) // 2, a['i'], a['e'] // 3, a['t']]), 0))
