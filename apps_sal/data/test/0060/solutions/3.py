s = input()
n = int(s[:-1]) - 1
s = s[-1]
res = n // 4 * (6 * 2 + 4)
if n % 2 == 1:
    res += 7
res += {'f': 1, 'e': 2, 'd': 3, 'a': 4, 'b': 5, 'c': 6}[s]
print(res)
