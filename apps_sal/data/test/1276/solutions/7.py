from collections import Counter as C
n = int(input())
S = list(input())
a = 1
L = C(S).most_common(3)
for l in L:
    a *= l[1]
for i in range(1, n):
    for j in range(n - 2 * i):
        if len(set((S[j], S[j + i], S[j + 2 * i]))) == 3:
            a -= 1
print(a if len(L) > 2 else 0)
