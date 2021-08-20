x = input()
n = int(x)
ln = len(x)
y = int(x[0])
y += 1
y = y * 10 ** (ln - 1)
print(y - n)
