n = input()
a = n[:-1]
b = n[:-2] + n[-1]
print(max(list(map(int, [a, b, n]))))
