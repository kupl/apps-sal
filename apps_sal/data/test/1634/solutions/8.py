a,b,c,d = map(int, input().split())
n, m = map(int, input().split())
t = list(map(int, input().split()))
h = list(map(int, input().split()))
v = []
w = []
for i in t:
    v.append(min(a*i, b))
for i in h:
    w.append(min(a*i,b))
t = min(c,sum(v))
h = min(c,sum(w))
print(min(d,t+h))
