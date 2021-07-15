tkhp,tkat,aohp,aoat = list(map(int,input().split()))

while True:
    aohp -= tkat
    if aohp <= 0:
        print('Yes')
        break
        
    tkhp -= aoat
    if tkhp <= 0:
        print('No')
        break
