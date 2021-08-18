S = input()
l = [S[0]]
a = 0
n = len(S)
f = S[0]
for i in range(1, n):
    if f != "L" or S[i] != "R":
        l[a] += S[i]
    else:
        l.append(S[i])
        a += 1
    f = S[i]

for x in l:
    r = x.count("R")
    t = len(x)
    a, b = divmod(t, 2)
    for i in range(r - 1):
        print("0", end=" ")
    if r % 2 == 0:
        print(a, end=" ")
        print(a + b, end=" ")
    else:
        print(a + b, end=" ")
        print(a, end=" ")
    for i in range(t - r - 1):
        print("0", end=" ")
