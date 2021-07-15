n = input()
s1,s2 = input(),input()
l2,l3 = [],[]
l1 = [[l2.append((s1[x] + s2[x],x)),l3.append((s2[x] + s1[x],x))] for x in range(len(s1)) if s1[x] != s2[x]]
d1,d2 = dict(l2),dict(l3)
ins = set(d1.keys()) & set(d2.keys())
if ins:
    e = ins.pop()
    print (len(l1) - 2)
    print (d1[e] + 1,d2[e] + 1)
    return
s1,s2 = {y[0][0]:y[1] for y in l2},{y[0][1]:y[1] for y in l2}
ins = set(s1.keys()) & set(s2.keys())
if ins:
    e = ins.pop()
    print (len(l1) - 1)
    print (s1[e] + 1,s2[e] + 1)
    return
print (len(l1))
print (-1,-1)
