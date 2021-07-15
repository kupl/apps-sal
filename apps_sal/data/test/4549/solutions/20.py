H,W=list(map(int,input().split()))

sq=[list(input()) for i in range(H)]

for i in range(H):
    for j in range(W):
        if sq[i][j]=="#":
            temp=0
            if j!=0:
                if sq[i][j-1]=="#":
                    temp+=1
            if j!=W-1:
                if sq[i][j+1]=="#":
                    temp+=1
            if i!=0:
                if sq[i-1][j]=="#":
                    temp+=1
            if i!=H-1:
                if sq[i+1][j]=="#":
                    temp+=1
            if temp==0:
                print("No")
                return

print("Yes")

