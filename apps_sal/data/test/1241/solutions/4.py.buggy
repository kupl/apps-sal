from collections import Counter
def mp(): return list(map(int, input().split()))
def lt(): return list(map(int, input().split()))
def pt(x): print(x)
def ip(): return input()
def it(): return int(input())
def sl(x): return [t for t in x]
def spl(x): return x.split()
def aj(liste, item): liste.append(item)
def bin(x): return "{0:b}".format(x)
def printlist(l): print(' '.join([str(x) for x in l]))


n, k = mp()
a = lt()
c = 0
maxx = 0
j = 0
index = None
if k == 0:
    w = ''.join([str(x) for x in a])
    y = max([len(m) for m in w.split("0")])
    print(y)
    printlist(a)
    return
for i in range(n):
    if i >= 1 and a[i - 1] == 0:
        c -= 1
    while j < n and c <= k:
        if a[j] == 0:
            c += 1
        j += 1
    if c > k:
        r = j - i - 1
    else:
        r = j - i
    if r > maxx:
        maxx = r
        if c > k:
            index = (i, j - 1)
        else:
            index = (i, j)
a[index[0]:index[1]] = [1] * (index[1] - index[0])
print(maxx)
printlist(a)
