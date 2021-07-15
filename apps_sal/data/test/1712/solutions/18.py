input=__import__('sys').stdin.readline
n,x,y=map(int,input().split())
ans=[]
cx=cy=1
for i in range(x+y-1):
    if cx/x>cy/y:ans.append(1);cy+=1
    elif cx/x<cy/y:ans.append(0);cx+=1
    else:ans.append(2);ans.append(2);cx+=1;cy+=1
f=['Vanya','Vova','Both']
for _ in range(n):
    n=int(input())-1
    print(f[ans[n%(x+y)]])
