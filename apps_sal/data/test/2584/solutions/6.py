t = int(input())
for i in range(t):
    n, p, k = [int(x) for x in input().split()]
    alist = [int(x) for x in input().split()]
    alist.sort()
    blist = [alist[0], alist[1]]
    for x in range(2, n):
        blist.append(blist[-2] + alist[x])
    for j in range(n):
        if p < blist[j]:
            break
    if p >= blist[j]:
        print(n)
    else:
        print(j)
