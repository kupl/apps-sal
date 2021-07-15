s = input()

sl = list(s)
sl.append("2")

n = len(sl)
res=[]

temp =1
for i  in range(n-1):
    if sl[i+1] == sl[i]:
        temp +=1
    else:
        res.append(temp)
        temp = 1

resu = n-1
m = n-1

while len(res) >1:
    resu = min(resu,max(res[0],m-res[0]))
    x = res.pop(1)
    res[0]  = res[0]+x    
    
print(resu)
