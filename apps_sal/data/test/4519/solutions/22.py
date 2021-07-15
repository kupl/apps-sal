t = int(input())
for test in range(t):
    n,k = [int(x) for x in input().split()]
    s = list(input())

    zer = []
    for i in range(n):
        if s[i]=='0':
            zer.append(i)
    curr = 0
    #print(s)
    while k>0 and curr<len(zer):
        if curr==0:
            swaps=zer[curr]
        else:
            swaps = zer[curr]-zer[curr-1]-1

        if swaps>k:
            swaps = k
        #print(swaps,'ss')
        if swaps==0:
            curr+=1
            continue

        x = zer[curr]
        y = x-swaps
        s[x]='1'
        #print(s,y)
        s[y]='0'
        k = k-swaps
        zer[curr]=y
        curr+=1
        #print(s)

    for i in range(n):
        print(s[i],end="")
    print()

