import sys
n = int(sys.stdin.readline())
e = dict()
w = dict()
for i in range(1, n+1):
    w[i] = -1
    e[i] = set()

for i in range(n-1):
    (a, b) = map(int, sys.stdin.readline().split())
    e[a].add(b)
    e[b].add(a)



first = 0
for i in e:
    if len(e[i]) == 1:
        first = i
        break


sosed = set()
posetil = set()
sosed.add(first)
posetil.add(first)
w[first] = 1

while len(sosed) > 0:
    sosed2 = set()
    for i in sosed:
        NO = set()
        NO.add(w[i])
        bad = set()
        for j in e[i]:
            if len(e[j]) > 1:
                sosed2.add(j)
            if w[j] != -1:
                NO.add(w[j])
            else:
                bad.add(j)
        x = 1
        for j in bad:
            if w[j] == -1:
                while x in NO:
                    x += 1
                w[j] = x
                NO.add(x)
        posetil.add(i)
    sosed2 -= posetil
    sosed = sosed2.copy()
ans = []
lol = set()
for i in range(1, n+1):
    ans.append(w[i])
    lol.add(w[i])
print(len(lol))
print(*ans)
