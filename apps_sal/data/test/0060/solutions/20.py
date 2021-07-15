s = input()
n = int(s[:-1])
last = s[-1]
if n % 4 in (1, 2):
    t = (n + 2) // 2
    b = 0
else:
    t = n // 2
    b = -2
bereza = {'f': 0, 'e': 1, 'd': 2, 'a': 3, 'b': 4, 'c': 5}
print((t - 1) * 6 + n + b + bereza[last])
