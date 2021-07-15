type=[[1,1,1,1,1,1,0],[0,0,1,1,0,0,0],[0,1,1,0,1,1,1],[0,1,1,1,1,0,1],[1,0,1,1,0,0,1],[1,1,0,1,1,0,1],[1,1,0,1,1,1,1],[0,1,1,1,0,0,0],[1,1,1,1,1,1,1],[1,1,1,1,1,0,1]]
def check(dis,x):
    for i in range(0,7):
        if(type[dis][i] and not type[x][i]):
            return False
    return True
(a,b)=input()
sum1=0
for i in range(0,10):
    if(check(int(a),i)):
        sum1+=1
sum2=0
for i in range(0,10):
    if(check(int(b),i)):
        sum2+=1
print(sum1*sum2)
