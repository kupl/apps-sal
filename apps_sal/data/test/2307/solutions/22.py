n = int(input())
a = [int(i) for i in input().split()]
c=0
for i in a:
    if i%2==0:
        c+=1
if c>n-c:
    print("READY FOR BATTLE")
else:
    print("NOT READY")

