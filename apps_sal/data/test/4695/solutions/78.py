x,y = map(int,input().split())
g = [[1,3,5,7,8,10,12],[4,6,9,11],[2]]
s = 0
for i in range(3):
    if x in g[i] and y in g[i]:
        print("Yes")
        s = 1
if s == 0:
    print("No")
