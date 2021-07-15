a, b = map(int, input().split())
s = input()
t = input()
sl = len(s)
tl = len(t)
mask = []
best = 0
besti = 0
for i in range(tl - sl + 1):
    eq = 0
    for j in range(sl):
        if t[i + j] == s[j]:
            eq += 1
    if eq > best:
        best = eq
        besti = i
for j in range(sl):
    if t[besti + j] != s[j]:
        mask.append(j + 1)
print(sl - best)
for i in mask:
    print(i, end=' ')

