n = int(input())
s = ''
i = 0
while len(s) < 1000:
    i += 1
    s += str(i)
print(s[n - 1])
