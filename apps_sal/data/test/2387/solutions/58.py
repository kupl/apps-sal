# input
N = int(input())
S = [input() for _ in range(N)]

# process
T = []
for s in S:
    while '()' in s:
        s = s.replace('()', '')
    T.append(s)

l1 = []
l2 = []
for t in T:
    op = t.find('(')
    if op < 0:
        op = len(t)
    cl = len(t) - op
    
    if cl+op != 0:
        if cl <= op:
            l1.append((cl, op))
        else:
            l2.append((op, cl))

l1.sort()
l2.sort(reverse=True)

result = False
x = 0
if len(l1)+len(l2) == 0:
    result = True
elif len(l1)>0 and len(l2)>0 and l1[0][0]+l2[-1][0] == 0:
    for cl, op in l1:
        x -= cl
        if x < 0:
            break
        x += op
    
    if x >= 0:
        for op, cl in l2:
            x -= cl
            if x < 0:
                break
            x += op
            
        if x == 0:
            result = True

# output
print(("Yes" if result else "No"))

