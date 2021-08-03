t = int(input())
for you in range(t):
    n = int(input())
    l = input().split()
    li = [int(i) for i in l]
    z = min(li)
    l1 = []
    hashimul = dict()
    for i in range(n):
        if(li[i] % z == 0):
            l1.append(li[i])
            hashimul[i] = len(l1) - 1
    l1.sort()
    lfi = []
    for i in range(n):
        if(i in hashimul):
            lfi.append(l1[hashimul[i]])
        else:
            lfi.append(li[i])
    poss = 1
    for i in range(1, n):
        if(lfi[i] < lfi[i - 1]):
            poss = 0
            break
    if(poss):
        print("YES")
    else:
        print("NO")
