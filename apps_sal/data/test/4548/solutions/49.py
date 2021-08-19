(N, M, X) = map(int, input().split())
L = list(map(int, input().split()))
s = 0
b = 0
for i in L:
    if i > X:
        s += 1
    else:
        b += 1
if s >= b:
    print(b)
else:
    print(s)
