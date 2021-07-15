a,b = map(int,input().split())
s = list(map(int,input().split()))
w = []

for i in range(b):
    w.append(min(s))
    s.remove(min(s))

print(sum(w))
