h, n = map(int, input().split())
A = list(map(int, input().split()))

tot = sum(A)
hp = h - tot
if(hp <= 0):
    print("Yes")
else:
    print("No")
