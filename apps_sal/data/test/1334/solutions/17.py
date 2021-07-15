n, k  = list(map(int, input().split()))
s = input()[:n]
digs = set(s)
mind = min(digs)
maxd = max(digs)
if n<k:
    print (s+mind*(k-n))
    return
for i in range(min(n,k)-1, -1, -1):
    if s[i]<maxd:
        biggerchars  = [ch for ch in digs if ch > s[i]]
        bestchar = min(biggerchars)
        res = s[:i] + bestchar + mind*(k-1-i)
        print (res)
        return
print(maxd*k)
