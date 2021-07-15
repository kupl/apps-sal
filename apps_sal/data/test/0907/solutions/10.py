n,m = map(int, input().strip().split())
can = False
pairs = []
for i in range (m):
    a,b = map(int, input().strip().split())
    pairs.append([a,b])
first = pairs[0][0]
missed = []
for i in range(m):
    if pairs[i][0] != first and pairs[i][1] != first:
        missed.append(i)
if missed != []:
    ind = missed[0]
    second = pairs[ind][0]
    test = True
    for i in range(len(missed)):
        if second != pairs[missed[i]][0] and second != pairs[missed[i]][1]:
            test = False
            break
    if test == True:
        can = True
    second = pairs[ind][1]
    test = True
    for i in range(len(missed)):
        if second != pairs[missed[i]][0] and second != pairs[missed[i]][1]:
            test = False
            break
    if test == True:
        can = True
else:
    can = True
# second half
first = pairs[0][1]
missed = []
for i in range(m):
    if pairs[i][0] != first and pairs[i][1] != first:
        missed.append(i)
if missed != []:
    ind = missed[0]
    second = pairs[ind][0]
    test = True
    for i in range(len(missed)):
        if second != pairs[missed[i]][0] and second != pairs[missed[i]][1]:
            test = False
            break
    if test == True:
        can = True
    second = pairs[ind][1]
    test = True
    for i in range(len(missed)):
        if second != pairs[missed[i]][0] and second != pairs[missed[i]][1]:
            test = False
            break
    if test == True:
        can = True
else:
    can = True
if can ==  True:
    print ('YES')
else:
    print ('NO')
