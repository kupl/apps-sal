s = input()
if len(s) >= 2:
    s = s[-2:]
s = int(s)
p = s % 4
r = [1, 1, 1, 1][p]
r += [1, 2, 4, 3][p]
r += [1, 3, 4, 2][p]
r += [1, 4, 1, 4][p]
r %= 5
print(r)
