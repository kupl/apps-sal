n = int(input())
word = []
endwith = [{} for i in range(5)]
second = []
first = {}
for i in range(n):
    w = input()
    word.append(w)
    c = 0
    lastkind = 0
    for ch in w:
        if ch == 'a':
            lastkind = 0
            c += 1
        elif ch == 'e':
            lastkind = 1
            c += 1
        elif ch == 'i':
            lastkind = 2
            c += 1
        elif ch == 'o':
            lastkind = 3
            c += 1
        elif ch == 'u':
            lastkind = 4
            c += 1
    if c not in endwith[lastkind]:
        endwith[lastkind][c] = [i]
    else:
        endwith[lastkind][c].append(i)
for i in range(5):
    for (key, value) in list(endwith[i].items()):
        while len(value) >= 2:
            second.append(value.pop())
            second.append(value.pop())
        if len(value) == 1:
            if key in first:
                first[key].append(value[0])
            else:
                first[key] = [value[0]]
ans = []
m = 0
for (key, value) in list(first.items()):
    while len(value) >= 2 and len(second) >= 2:
        ans.append((value.pop(), value.pop(), second.pop(), second.pop()))
        m += 1
while len(second) >= 4:
    ans.append((second.pop(), second.pop(), second.pop(), second.pop()))
    m += 1
print(m)
for tup in ans:
    print(word[tup[0]], word[tup[2]])
    print(word[tup[1]], word[tup[3]])
