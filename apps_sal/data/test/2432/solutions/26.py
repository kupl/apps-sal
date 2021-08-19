s = bin(int(input()))[2:]
s = '0' * (7 - len(s)) + s
res = list('0' * 7)
a = [0, 1, 6, 4, 3, 5, 2]
for i in range(7):
    res[i] = s[a[i]]
print(int(''.join(res), 2))
