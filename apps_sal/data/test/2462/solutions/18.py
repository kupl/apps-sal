import sys
input = sys.stdin.readline
for f in range(int(input())):
    n=int(input())
    if n>30:
        print("YES")
        if n-30 not in [6,10,14]:
            print(6,10,14,n-30)
        else:
            if n-30==6:
                print(5,6,10,15)
            if n-30==10:
                print(6,9,10,15)
            if n-30==14:
                print(6,10,13,15)
    else:
        print("NO")
