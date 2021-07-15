n=int(input())


for nombre in range(0,n+1,1234567):
        for nombre2 in range(0,n+1,123456):
                reste=(n-nombre-nombre2)%1234
                diviseur=(n-nombre-nombre2)//1234
                if diviseur>=0 and reste==0:
                        print("YES")
                        return
print("NO")

