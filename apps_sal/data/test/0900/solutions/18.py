
s = input()
n = len(s)
dp1 =[0 for _ in range(13)]
dp1[0]=1


move = [[] for _ in range(13)]

for i in range(10):
    for j in range(13):
        move[(10*j+i)%13].append(j)



for i in range(n):
    dp2 =[0 for _ in range(13)]
    if s[i]=="?":
        si = list(range(10))
        for mod,ex in enumerate(move):
            dp2[mod] += sum([dp1[x] for x in ex])
    else:
        si = int(s[i])
        for j in range(13):
            dp2[(10*j+si)%13]+=dp1[j]
    dp1 = [x%(10**9+7) for x in dp2] 


print((dp1[5]))

