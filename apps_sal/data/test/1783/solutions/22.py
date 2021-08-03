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


n, k = mp()
a = lt()

s = sum(a[:k])
l = 0
for i in range(n - k + 1):
    l += s
    if i + k < n:
        s += (a[i + k] - a[i])
pt(l / (n - k + 1))
