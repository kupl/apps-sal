s = input()
x = int(s)
y = int(str(int(s[0]) + 1) + '0' * (len(s) - 1))
print(y - x)
