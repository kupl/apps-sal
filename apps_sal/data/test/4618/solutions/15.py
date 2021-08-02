s = input()
k = int(input())
n = len(s)
subst = set()
for i in range(n):
    for j in range(5):
        subst.add(s[i:i + j + 1])
ls = list(subst)
ls.sort()
print((ls[k - 1]))
