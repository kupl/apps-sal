import string
n = int(input())
s = list(str(input()))
m = int(input())
l = []
result = 0
for i in range(m):
    l.append(list(str(input())))
index = []
have = []
for i in range(n):
    if s[i] == '*':
        index.append(i)
    else:
        have.append(s[i])
have = set(have)
t = [1 for i in range(m)]
c = len(index)
for i in range(m):
    for j in index:
        if (l[i])[j] in have:
            t[i] = 0
            break
for j in range(m):
    for i in range(n):
        if i not in index:
            if (l[j])[i] != s[i]:
                t[j] = 0
                break

new = []
for i in range(m):
    if t[i] == 1:
        new.append(l[i])

alph = list(string.ascii_lowercase)
for i in have:
    alph.remove(i)
ll = len(new)
for i in alph:
    count = 0
    for j in range(len(new)):
        for k in index:
            if (new[j])[k] == i:
                count += 1
                break
    if count == ll:
        result += 1
print(result)
