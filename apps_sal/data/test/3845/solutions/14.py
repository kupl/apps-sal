a,b=list(map(int,input().split()))
grid=[["." for i in range(100)] for j in range(50)]+[["#" for i in range(100)] for j in range(50)]
white=0;black=0
for i in range(49):
    if black==b-1:break
    if i%2==0:continue
    for j in range(100):
        if i%2==j%2:
            grid[i][j]="#"
            black+=1
        if black==b-1:break
    
for i in range(50,100):
    if white==a-1:break
    if i%2==0:continue
    for j in range(100):
        if i%2==j%2:
            grid[i][j]="."
            white+=1
        if white==a-1:break
print((100,100))
for i in range(100):
    stri=""
    for j in grid[i]:
        stri+=j
    print(stri)

