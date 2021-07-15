n=eval(input())
a=list(map(int,input().split()))
e=o=0
for i in range(n):
    if a[i]%2:
        o+=1
    else:
        e+=1
if e>o:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
