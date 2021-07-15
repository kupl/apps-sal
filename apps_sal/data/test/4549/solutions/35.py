h,w = list(map(int,input().split()))
s = [list(input()) for _ in range(h)]

dxy = [(1,0),(0,1),(-1,0),(0,-1)]
ans = True
for i in range(h):
    for j in range(w):
        cnt = 0
        if s[i][j]=="#":
            for p,q in dxy:
                if not(0<=i+p<h and 0<=j+q<w):
                    cnt += 1 
                    continue
                elif s[i+p][j+q] == ".":
                    cnt += 1
                else:
                    continue
        if cnt == 4:
            ans = False
print(("Yes" if ans==True else "No"))


