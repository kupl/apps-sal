X,Y = map(int,input().split())
turu = 2
kame = 4
for i in range(X+1):
    ans = turu * i + kame*(X-i)
    if ans == Y:
        print("Yes")
        return
print("No")
