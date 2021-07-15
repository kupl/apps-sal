n=int(input())
a=map(int,input().split())
d=dict()
acc=0
for v in a:
    acc += v
    if acc in d:
        d[acc] += 1
    else:
        d[acc] = 1
print(n-max(d.values()))
