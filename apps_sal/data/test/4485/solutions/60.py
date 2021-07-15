N,M = map(int,input().split())
I = set()
n = set()
for i in range(M):
    a,b = map(int,input().split())
    if a == 1:
        I.add(b)
    if b == 1:
        I.add(a)
    if a == N:
        n.add(b)
    if b == N:
        n.add(a)
if  I & n == set():
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
