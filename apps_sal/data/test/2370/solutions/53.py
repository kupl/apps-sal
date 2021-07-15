def main():
    inf=float("inf")
    n=int(input())
    alst=[list(map(int,input().split())) for _ in range(n)]
 
    for i in range(n):
        alst[i][i]=inf
 
    sm=0
    token=0
 
    for i in range(n):
        for j in range(i+1,n):
            for k in range(n):
                if alst[i][k]+alst[k][j]>alst[i][j]:
                    continue
                elif alst[i][k]+alst[k][j]==alst[i][j]:
                    break
                else:
                    token=1
                    break
            else :
                sm+=alst[i][j]
    
    if token : sm=-1
 
    print(sm)
 
main()
