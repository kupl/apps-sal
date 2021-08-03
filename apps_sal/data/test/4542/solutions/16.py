s = input()
c = 0
t = s[0]
for k in s[1:]:
    if t != k:
        t = k
        c += 1
print(c)
