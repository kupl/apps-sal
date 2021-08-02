t = int(input())
for i in range(t):
    la = []
    ra = []
    n = int(input())
    for j in range(n):
        l, r = list(map(int, input().split()))
        la.append(l)
        ra.append(r)
    x = max(la) - min(ra)
    if x < 0:
        x = 0
    print(x)
