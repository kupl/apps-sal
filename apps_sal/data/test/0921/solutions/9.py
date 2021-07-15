def mp():  return list(map(int,input().split()))
def lt():  return list(map(int,input().split()))
def pt(x):  print(x)
def ip():  return input()
def it():  return int(input())
def sl(x):  return [t for t in x]
def spl(x): return x.split()
def aj(liste, item): liste.append(item)
def bin(x):  return "{0:b}".format(x)
def listring(l): return ' '.join([str(x) for x in l])
def ptlist(l): print(' '.join([str(x) for x in l]))

n,w = mp()
a = lt()
b = [int((a[i]+1)/2) for i in range(n)]
if sum(b) <= w:
    d = w - sum(b)
    c = sorted([i for i in range(n)],key=lambda x: a[x],reverse = True)
    while d > 0:
        i = c[0]
        r = min(d,a[i]-b[i])
        d -= r
        b[i] += r 
        c.pop(0)
    ptlist(b)
else:
    pt(-1)

