S = input()
i = 1
l = len(S)
res = 0
f = S[0]

while i < l:
    if (S[i] == f):
        i += 1
    else:
        res += 1
        f = S[i]
        i += 1
print(res)
