n,m = map(int,input().split())
for i in range(m):
    r,l = map(int, input().split())
for i in range(n):
    if(i%2 == 0):
        print("0", end = "")
    else:
        print("1", end = "")

