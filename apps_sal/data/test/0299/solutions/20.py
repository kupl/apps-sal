n = int(input())
t = [int(x) for x in input().split()]
c = bi = ba = 0
for ii in range(n):
    if (ii + 1) % 3 == 1:
        c += t[ii]
    elif (ii + 1) % 3 == 2:
        bi += t[ii]
    else:
        ba += t[ii]
if c > bi and c > ba:
    print('chest')
elif bi > c and bi > ba:
    print('biceps')
else:
    print('back')
