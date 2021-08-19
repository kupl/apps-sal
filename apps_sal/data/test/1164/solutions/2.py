# You lost the game.
s = str(input())
n = len(s)
i = 0
r = 0
A = "0123456789."
while i < n:
    while A.count(s[i]) == 0:
        i += 1
    p = ""
    while i < n and A.count(s[i]):
        p += s[i]
        i += 1
    E = list(p.split("."))
    # print(p,E)
    e = len(E)
    if len(E[e - 1]) == 2:
        v = 0
        for j in range(e - 1):
            v = v * 1000 + int(E[j])
        v = v * 100 + int(E[e - 1])
    else:
        v = 0
        for j in range(e):
            v = v * 1000 + int(E[j])
        v *= 100
    r += v
# print(r)
R = str(r)
m = len(R) - 2
res = ""
if m > 0:
    res = R[:m % 3]
    for i in range(m % 3, m, 3):
        if i > 0:
            res += "." + R[i:i + 3]
        else:
            res += R[i:i + 3]
if m <= 0:
    res += "0"
if m == -1:
    res += ".0" + R[m + 1]
elif R[m:m + 2] != "00":
    res += "." + R[m:m + 2]

print(res)
