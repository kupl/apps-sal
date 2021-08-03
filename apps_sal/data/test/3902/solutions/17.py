import sys
sys.setrecursionlimit(10000)

s = input()
s = s[5:] + " "
res = set()
aux = set()


def getWords(x, y):
    if (x, y) in aux:
        return
    aux.add((x, y))
    if x > 1 and s[x:y] != s[x - 2:x]:
        res.add(s[x - 2:x])
        getWords(x - 2, x)
    if x > 2 and s[x:y] != s[x - 3:x]:
        res.add(s[x - 3:x])
        getWords(x - 3, x)


getWords(len(s) - 1, len(s))

print(len(res))
for word in sorted(list(res)):
    print(word)
