n = int(input())
word = input()

ast = word.count('*')
mas = [i for i in range(n) if word[i] == '*']
mas1 = [i for i in range(n) if word[i] != '*']
st = {word[i] for i in mas1}

m = int(input())
Mas = list()
for i in range(m):
    temp = input()
    f = True
    for j in mas1:
        if temp[j] != word[j]:
            f = False
            break
    if f:
        t = [temp[k] for k in mas if temp[k] not in st]
        if len(t) == ast:
            Mas.append(set(t))

ans = set()
for el in Mas:
    ans |= el

count = 0
for i in ans:
    f = True
    for j in Mas:
        if i not in j and len(j) > 0:
            f = False
            break
    if f:
        count += 1

print(count)
