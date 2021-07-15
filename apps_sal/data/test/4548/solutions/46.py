n,m,x = list(map(int, input().split()))
a = list(map(int, input().split()))
c0 = 0
cN = 0
for A in a:
    if A > x:
        cN += 1
    elif A < x:
        c0 += 1
print(min(c0, cN))
