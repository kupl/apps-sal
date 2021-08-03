s = input()
l = len(s) - 1
res = 0
for i in range(2**l):
    t = s[0]
    for j in range(l):
        if i & (1 << j):
            t += "+"
        t += s[j + 1]
    res += eval(t)
print(res)
