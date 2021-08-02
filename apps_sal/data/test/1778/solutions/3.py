n = int(input())
s = input().split()
la = [int(s[i]) for i in range(n)]
s = input().split()
lb = [int(s[i]) for i in range(n)]
la.sort()
lb.sort()
sa = 0
sb = 0
for i in range(n):
    if len(la) == 0:
        if len(lb) > 0:
            del(lb[-1])
        else:
            break
    elif len(lb) == 0:
        sa += la[-1]
        del(la[-1])
    elif la[-1] > lb[-1]:
        sa += la[-1]
        del(la[-1])
    else:
        del(lb[-1])

    if len(lb) == 0:
        if len(la) > 0:
            del(la[-1])
        else:
            break
    elif len(la) == 0:
        sb += lb[-1]
        del(lb[-1])
    elif lb[-1] > la[-1]:
        sb += lb[-1]
        del(lb[-1])
    else:
        del(la[-1])
print(sa - sb)
