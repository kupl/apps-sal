from copy import deepcopy
def mp(): return list(map(int, input().split()))
def lt(): return list(map(int, input().split()))
def pt(x): print(x)
def ip(): return input()
def it(): return int(input())
def sl(x): return [t for t in x]
def spl(x): return x.split()
def aj(liste, item): liste.append(item)
def bin(x): return "{0:b}".format(x)
def listring(l): return ' '.join([str(x) for x in l])
def ptlist(l): print(' '.join([str(x) for x in l]))


c, b, h, w, n = mp()
d = lt()
d.sort(reverse=True)
k = min(n, 34)
a = d[:k]
if (c <= h and b <= w) or (c <= w and b <= h):
    pt(0)
else:
    dict = {h: w}
    i = 0
    bl = True
    while bl and i < k:
        x = a[i]
        dict1 = {}
        for r in dict:
            if r * x in dict1:
                dict1[r * x] = max(dict1[r * x], dict[r])
            else:
                dict1[r * x] = dict[r]
            if r in dict1:
                dict1[r] = max(dict1[r], dict[r] * x)
            else:
                dict1[r] = dict[r] * x
        if any((r >= c and dict1[r] >= b) or (r >= b and dict1[r] >= c) for r in dict1):
            bl = False
        else:
            i += 1
            dict = deepcopy(dict1)
    if i == k:
        pt(-1)
    else:
        pt(i + 1)
