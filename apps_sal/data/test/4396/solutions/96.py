n=int(input())
J,B=0,0
for i in range(n):
    x,u=map(str,input().split())
    if u=="JPY":
        J+=int(x)
    else:
        B+=float(x)

ans=J+B*380000
print(ans)
