n = int(input())
a = list(map(int, input().split()))
l = 0
r = n - 1
ot = []
prot = ''
if a[l] < a[r]:
    ot.append(a[l])
    l += 1
    prot += 'L'
else:
    ot.append(a[r])
    r -= 1
    prot += 'R'
run = True
while run:
    if l > r:
        run = False
    elif l == r:
        if a[l] >= ot[-1]:
            prot += 'R'
        run = False
    elif ot[-1] <= a[l] <= a[r]:
        ot.append(a[l])
        l += 1
        prot += 'L'
    elif ot[-1] <= a[r] <= a[l]:
        ot.append(a[r])
        r -= 1
        prot += 'R'
    elif ot[-1] <= a[l]:
        ot.append(a[l])
        l += 1
        prot += 'L'
    elif ot[-1] <= a[r]:
        ot.append(a[r])
        r -= 1
        prot += 'R'
    else:
        run = False
print(len(prot))
print(prot)
