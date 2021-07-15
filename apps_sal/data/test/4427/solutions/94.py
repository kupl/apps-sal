r,d,x = list(map(int,input().split()))
su = 0
for i in range(10):
    su = r*x - d
    print(su)
    x = su
    su = 0

