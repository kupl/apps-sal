n,a,b,k,f = [int(i) for i in input().split()]
pred = "_"
d = dict()
for i in range(n):
    s1, s2 = [i for i in input().split()]
    pr = a
    if s1 == pred:
        pr = b

    if (s1, s2) in list(d.keys()):
        d[(s1, s2)] += pr
    elif (s2, s1) in list(d.keys()):
        d[(s2, s1)] += pr
    else:
        d[(s1, s2)] = pr

    pred = s2
    
cn = k
ans = sum(d.values())
for i in sorted(list(d.values()), reverse = True):
    if cn == 0 or i <= f:
        break
    ans = ans - i + f
    cn -= 1

print(ans)
    

