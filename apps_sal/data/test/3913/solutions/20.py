c = input()
s = input()

star = []
no_star = []
for i in range(len(s)):
    if s[i] == '*':
        star.append(i)
    else:
        no_star.append(i)

n = int(input())
d = {}
skip = 0
for i in range(n):
    s1 = input()
    ext = 0
    for i in no_star:
        if s1[i] not in s:
            ext = 1
    for i in star:
        if s1[i] in s:
            ext = 1
            break
    if ext == 1:
        skip+=1
        continue
    mas = []
    for i in star:
        mas.append(s1[i])
    mas = list(set(mas))
    for i in mas:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
ans = 0
for i in d:
    if d[i] == n-skip:
        ans+=1
print (ans)

