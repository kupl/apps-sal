n, k = [int(i) for i in input().split()]
s = list(input())
l = len(s)
d = {}
f = [True] * l
for i in range(l):
    if not s[i] in d:
        d[s[i]] = []
    d[s[i]].append(i)

rule = []
for i in range(26):
    wk1 = chr(i + 97)
    if wk1 in d:
        rule.append(wk1)

current = 0
position = 0
for i in range(k):
    f[d[rule[current]][position]] = False
    position += 1
    if position == len(d[rule[current]]):
        position = 0
        current += 1
    if current == len(rule):
        break

for i in range(l):
    if f[i]:
        print(s[i], end="")
print()
