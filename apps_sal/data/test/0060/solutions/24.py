l = input()
n = int(l[:-1])
s = l[-1]

d = {'a': 4, 'b': 5, 'c': 6, 'd': 3, 'e': 2, 'f': 1}

k = (n - 1) // 4
res = 16 * k
if n % 4 in [0, 2]:
    res += 7
res += d[s]
print(res)
