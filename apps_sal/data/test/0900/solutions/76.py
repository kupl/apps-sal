inf = 10**9 + 7
s = input()
r = [[(j-k)*9%13 for j in range(10)] for k in range(13)]
d = [1] + [0]*12
for c in s:
    d = [sum(d[j] for j in k)%inf for k in r] if c > '9' else [d[(int(c)-k)*9%13] for k in range(13)]
print((d[5]))

