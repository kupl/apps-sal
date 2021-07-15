N,R = map(int,input().split())

if N >= 10:
    print(R)

else:
    r = 100*(10-N)
    print(r+R)
