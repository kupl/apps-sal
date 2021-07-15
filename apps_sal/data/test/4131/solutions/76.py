n,m=map(int,input().split())
PY=[list(map(int,input().split())) for _ in range(m)]
for i in range(m):
    PY[i].append(i)
py=sorted(PY)
ans=[None]*m
#print(py,PY)
tmp_y=1
for i in range(m):
    if i>0:
        if py[i][0]!=py[i-1][0]:
            tmp_y=1
        else:
            tmp_y+=1
    ans_l="0"*(6-len(str(py[i][0])))+str(py[i][0])
    ans_r="0"*(6-len(str(tmp_y)))+str(tmp_y)
    #print(ans_l+ans_r)
    ans[py[i][2]]=ans_l+ans_r
[print(i) for i in ans]
