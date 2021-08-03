def mp(): return list(map(int, input().split()))
def lt(): return list(map(int, input().split()))
def pt(x): print(x)
def ip(): return input()
def it(): return int(input())
def sl(x): return [t for t in x]
def spl(x): return x.split()
def aj(liste, item): liste.append(item)
def bin(x): return "{0:b}".format(x)


n = it()
L = lt()


def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)


c = 0
i = 0
while i + 1 < len(L):
    d = gcd(L[i], L[i + 1])
    if d != 1:
        L.insert(i + 1, 1)
        c += 1
    i += 1
print(c)
print(' '.join([str(x) for x in L]))
