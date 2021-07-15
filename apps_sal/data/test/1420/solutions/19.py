n,l = map(int,input().split())
di = list(map(int,input().split()))
di = sorted(di)
maximum = 0
for i in range(n-1):
    if di[i+1]-di[i]>maximum:
        maximum = di[i+1]-di[i]
if float(maximum)/2 > di[0] and float(maximum)/2 > l - di[-1]:
    if maximum % 2== 0:
        print(maximum//2,end=".0000000000")
    else:
        print(maximum//2,end=".5000000000")
elif l - di[-1]>di[0]:
    print(l - di[-1],end=".0000000000")
else:
    print(di[0],end=".0000000000")

