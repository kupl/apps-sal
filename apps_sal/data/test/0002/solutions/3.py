n = int(input())
s = str(n)
s = str(int(s[0]) + 1) + '0' * (len(s) - 1)
s = int(s)
print(s - n)
