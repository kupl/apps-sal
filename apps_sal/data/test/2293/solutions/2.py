import sys
input = sys.stdin.readline

m,n=list(map(int,input().split()))

D=[set(list(map(int,input().split()))[1:]) for i in range(m)]


for i in range(m-1):
    for j in range(1,m):
        if D[i] & D[j]== set():
            print("impossible")
            return
else:
    print("possible")


