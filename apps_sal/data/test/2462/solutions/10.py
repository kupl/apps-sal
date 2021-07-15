# import sys
# input=sys.stdin.readine

t=int(input())
for _ in range(t):
    n=int(input())
    if n<=30:
        print("NO")
    else:
        if n-30 not in set([6,10,14]):
            print("YES")
            print(*sorted([6,10,14,n-30]))
        else:
            print("YES")
            print(*sorted([6,10,15,n-31]))
