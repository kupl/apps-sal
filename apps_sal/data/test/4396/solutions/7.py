n=int(input())
kei = 0.0
for i in range(n):
    x,u=map(str,input().split())
    if u=="JPY":
        kei += float(x)
    else:
        kei += float(x)*380000.0
print(kei)
