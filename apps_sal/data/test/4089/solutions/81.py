N = int(input())
c = 0
while N - 26**c >= 0:
    N -= 26**c
    c += 1

d = [0] * (c - 1)

i = 0
for i in range(c):
    d.insert(c - 1, N % 26)
    N = (N - d[i]) // 26
    i += 1
# print(d)
e = []
s = ''
for i in range(2 * c - 1):
    e.append(chr(97 + d[i]))
    s += e[i]
print((s[c - 1:2 * c - 1]))
# 1000000000000001
# zzzzzz
# 321272416
