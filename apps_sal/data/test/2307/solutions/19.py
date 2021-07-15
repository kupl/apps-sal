n=eval(input())
l=[int(x)&1 for x in input().split()]
if sum(l)<len(l)-sum(l):
    print("READY FOR BATTLE")
else:
    print("NOT READY")
    
