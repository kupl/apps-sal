p, n = map(int, input().split())
xlist = []
for i in range(n):
    xlist.append(int(input()))

remainderlist = []
for i in range(n):
    if xlist[i] % p not in remainderlist:
        remainderlist.append(xlist[i] % p)
    else:
        print(i + 1)
        quit()

print(-1)
