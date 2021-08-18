
s = str(input())
n = len(s)
L = [s]


def ok(L, s):
    for x in L:
        if x == s:
            return 0
    return 1


for i in range(n):
    s = s[1:] + s[0]
    if ok(L, s):
        L += [s]

print(len(L))
