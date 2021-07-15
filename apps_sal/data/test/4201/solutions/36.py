from copy import deepcopy

h,w,kkk = map(int,input().split())
c = [list(input()) for _ in range(h)]

cnt=0

for i in range(2**h-1):

    nuritubu_row=[]
    for k in range(i):
        if i>>k&1:
            nuritubu_row.append(k)

    
    for j in range(2**w-1):

        nuritubu_col=[]
        for k in range(j):
            if j>>k&1:
                nuritubu_col.append(k) 
                   
        c_tmp=deepcopy(c)
        for x in range(h):
            for y in range(w):
                if ((x in nuritubu_row) or (y in nuritubu_col)):
                    c_tmp[x][y]="o"        
                    
        if sum([c_tmp[k].count("#") for k in range(h)])==kkk:
            cnt+=1

print(cnt)
