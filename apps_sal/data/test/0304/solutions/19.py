def fact(n):
    nonlocal fa
    if fa[n] != -1:
        return fa[n]
    else:
        fa[n] = fact(n - 1) * n
        return fa[n]


fa = [-1] * 20
fa[0] = 1
fa[1] = 1
fa[2] = 2

res = 0

a = int(input())
b = str(a)
s = [0] * 10
for i in range(len(b)):
    s[int(b[i])] += 1

for i0 in range(s[0] + 1):
    if i0 > 0 or s[0] == 0:
        for i1 in range(s[1] + 1):
            if i1 > 0 or s[1] == 0:
                for i2 in range(s[2] + 1):
                    if i2 > 0 or s[2] == 0:
                        for i3 in range(s[3] + 1):
                            if i3 > 0 or s[3] == 0:
                                for i4 in range(s[4] + 1):
                                    if i4 > 0 or s[4] == 0:
                                        for i5 in range(s[5] + 1):
                                            if i5 > 0 or s[5] == 0:
                                                for i6 in range(s[6] + 1):
                                                    if i6 > 0 or s[6] == 0:
                                                        for i7 in range(s[7] + 1):
                                                            if i7 > 0 or s[7] == 0:
                                                                for i8 in range(s[8] + 1):
                                                                    if i8 > 0 or s[8] == 0:
                                                                        for i9 in range(s[9] + 1):
                                                                            if i9 > 0 or s[9] == 0:
                                                                                w2 = [i0, i1, i2, i3, i4, i5, i6, i7, i8, i9]
                                                                                su = 0
                                                                                for i in range(10):
                                                                                    su += w2[i]
                                                                                for i in range(1, 10):
                                                                                    if w2[i] > 0:
                                                                                        w2[i] -= 1
                                                                                        su -= 1

                                                                                        res += fact(su) / (fact(w2[0]) * fact(w2[1]) * fact(w2[2]) * fact(w2[3]) * fact(w2[4]) * fact(w2[5]) * fact(w2[6]) * fact(w2[7]) * fact(w2[8]) * fact(w2[9]))

                                                                                        su += 1
                                                                                        w2[i] += 1
print(int(res))
