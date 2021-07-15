n=int(input())

l=list((v*h) for h in range(1,10) for v in range(1,10))

if n in l:
    print("Yes")
else:
    print("No")
