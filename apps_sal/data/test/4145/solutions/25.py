x=int(input())
#any()内で一個でもtrueであればtrueを返す
while any(x%i<1 for i in range(2,x)):
    x+=1
print(x)
