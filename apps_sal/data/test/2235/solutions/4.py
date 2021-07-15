n=int(input())
ex1=0
ex2=0
L=[]
f=[0]*(n+1)
for i in range(n):
    L.append(int(input()))
    while (L[i] - L[ex1 ] >= 90):
        ex1+=1
    while (L[i] - L[ex2 ] >= 1440):
        ex2+=1
    f[i+1] = min(min(f[ex1] + 50, f[ex2] + 120), f[i] + 20)
    print(f[i+1] - f[i])

