H,W,N = map(int,input().split())
Nli=[]
for k in range(N):
    a,b=map(int,input().split())
    for n in range(-1,2):
        for m in range(-1,2):
            if 0<=a-2-m<H-2 and 0<=b-2-n<W-2:
                Nli.append((b-n)*(H)+(a-m))
import collections
s = collections.Counter(Nli)
v = list(s.values())
print((H-2)*(W-2)-len(set(Nli)))
for k in range(1,10):
    print(v.count(k))
