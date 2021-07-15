t=int(input())
for you in range(t):
    l=input().split()
    r=int(l[1])
    l=int(l[0])
    if(r<2*l):
        print("YES")
    else:
        print("NO")

