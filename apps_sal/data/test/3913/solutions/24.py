l = int(input())
secret = input()
indexes = []
noLetters = []
alph = ""

for i in range(len(secret)):
    if secret[i] == "*":
        indexes.append(i)
    else:
        noLetters.append(secret[i])

n = int(input())
dico = []
for _ in range(n):
    word = input()
    s = ""
    ok = True
    for i in range(len(word)):
        if i in indexes and word[i] not in noLetters:
            s += word[i]
        elif word[i] != secret[i]:
            ok = False
            break
    if ok and s != "" and s not in dico:
        dico.append(s)
        for c in s:
            if c not in alph:
                alph += c

total = 0
for c in alph:
    ok = True
    for w in dico:
        if c not in w:
            ok = False
            break
    if ok:
        total += 1
print(total)
