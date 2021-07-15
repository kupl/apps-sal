N = int(input())
Plist = list(map(int,input().split()))
Place = [0]*(N+1)
maxP = max(Plist)
for i in range(N):
    p = Plist[i]
    Place[p] = i+1
Plist = [0]+Plist
ans = 0
Nset = []
Na = set()
for i in range(N):
    maxplace = Place[maxP]
    while maxplace != maxP:
        if maxplace not in Na:
            Place[maxP] += 1
            a = Plist[maxplace+1]
            Place[a] -= 1
            Plist[maxplace] = a
            Plist[maxplace+1] = maxP
            Nset.append(maxplace)
            Na.add(maxplace)
            maxplace += 1
        else:
            ans = -1
            break
    maxP -= 1
if ans == -1:
    print(ans)
else:
    if len(Nset) == N-1:
        for n in Nset:
            print(n)
    else:
        print(-1)
