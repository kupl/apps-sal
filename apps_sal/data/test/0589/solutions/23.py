def f(x, k):
    res = 1
    for i in range(k - x, k):
        res *= i
    return res
    
t = input()
s, k = set(), t.count('?')

for i in t:
    if i >= 'A': s.add(i)

if t[0] in '123456789': print(f(len(s), 11) * 10 ** k)
elif t[0] == '?': print(f(len(s), 11) * 9 * 10 ** (k - 1))
else: print(9 * f(len(s) - 1, 10) * 10 ** k)

