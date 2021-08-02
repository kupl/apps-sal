s = input()
K = int(input())

subst = []
for i in range(5):
    for j in range(len(s) - i):
        subst.append(s[j:j + i + 1])

subst = list(set(subst))
subst.sort()

print(subst[K - 1])
