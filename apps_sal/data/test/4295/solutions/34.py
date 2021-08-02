n, k = list(map(int, input().split()))
r = n % k
l = []
while(not l.count(r)):
    l.append(r)
    r = abs(r - k)
l = sorted(l)
print((str(l[0])))
