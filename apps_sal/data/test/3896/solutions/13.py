s = input()
a = int(s, 2)
n = len(s)
print((a * (2**(n - 1))) % 1000000007)
