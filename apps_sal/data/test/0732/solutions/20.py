def find(x):
    if 0<x<=n:
        p.add(x)
        x*=10
        find(x+i)
        find(x+j)
n=int(input())
p= set()
for i in range(10):
    for j in range(10):
        find(i)
print(len(p))


