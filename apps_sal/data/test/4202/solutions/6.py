L,R = map(int,input().split())
if R-L+1 >= 2019:
    print(0)
    return
R %= 2019
L %= 2019
if R <= L:
    print(0)
    return
ans = float("inf")
for i in range(L,R):
    for j in range(i+1,R+1):
        ans = min(ans,(i*j)%2019)
print(ans)
