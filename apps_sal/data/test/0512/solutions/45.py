n = int(input())
inout = [[0,0] for i in range(2*n+1)]

for i in range(n):
    a,b = map(int,input().split())
    if a!=-1: 
        if inout[a]==[0,0]:
            inout[a] = [i+1,b]
        else:
            print('No')
            return
    if b!=-1:
        if inout[b]==[0,0]:
            inout[b] = [-i-1,a]
        else:
            print('No')
            return
            
ans = [False for i in range(n+1)]
ans[0] = True

for OUT in range(2,2*n+1,2):
    for IN in range(1,OUT+1,2):
        if ans[IN//2]:
            flg=True
            for i in range(IN,IN+(OUT-IN+1)//2):
                x=inout[i]
                y=inout[i+(OUT-IN+1)//2]
                if x==[0,0] and y==[0,0]:
                    continue
                elif x==[0,0]:
                    if y[0]>0 or y[1]!=-1:
                        flg=False
                        break
                elif y==[0,0]:
                    if x[0]<0 or x[1]!=-1:
                        flg=False
                        break
                else:
                    if x[0]!=-y[0] or x[0]<0:
                        flg=False
                        break
                    elif x[1]!=i+(OUT-IN+1)//2 or y[1]!=i:
                        flg=False
                        break
            if flg==False: continue
            ans[OUT//2]=True
if ans[-1]:
    print("Yes")
else:
    print("No")
