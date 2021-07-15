import itertools

L,R = list(map(int,input().split()))
if R - L + 1 >= 2019:
    ans = 0
else:
    LL = L % 2019
    RR = R % 2019
    if LL < RR:
        Amari_List = list(range(LL,RR+1))
        ans = 2019
        for v1,v2 in itertools.combinations(Amari_List, 2):
            ca = (v1*v2) % 2019 
            if  ca < ans:
                ans = ca
    else:
        ans = 0

print(ans)




