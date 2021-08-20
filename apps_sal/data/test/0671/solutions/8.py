n = int(input())
s = ''
i = 1
while len(s) < n:
    k = str(i)
    for j in range(len(k)):
        s += k[j]
    i += 1
print(s[n - 1])
