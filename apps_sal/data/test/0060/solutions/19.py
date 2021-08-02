d = {'f': 0, 'e': 1, 'd': 2, 'a': 3, 'b': 4, 'c': 5}
s = input()
n = int(s[:-1])
if n % 4 in (1, 2):
    st = (n + 2) // 2
    hui = 0
else:
    st = n // 2
    hui = -2
print((st - 1) * 6 + n + hui + d[s[-1]])
