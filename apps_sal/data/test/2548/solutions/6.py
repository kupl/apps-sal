q = int(input())
for _ in range(q):
    n = int(input())
    s = list(input())
    s = list(map(int,s))
    l = [s[i] - 1 for i in range(n)]
    pref = [0] * (n+1)
    for i in range(1,n+1):
        pref[i] = pref[i-1] + l[i-1]
    d = {}
    for elt in pref:
        try:
            d[elt] += 1
        except Exception:
            d[elt] = 1
    wyn = 0
    for elt in d:
        wyn += (d[elt]*(d[elt]-1)//2)
    print(wyn)
