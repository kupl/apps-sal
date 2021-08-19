p = 1000000007
s = input()
print(int(s, 2) * pow(2, len(s) - 1) % p)
