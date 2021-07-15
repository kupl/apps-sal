N,M=map(int,input().split())
String=[str(0) for _ in range(N)] #indexは0からに注意
flag=1
for _ in range(M):
    s,c=map(int,input().split())
    if c!=String[s-1] and String[s-1]!=str(0):
        flag=0
    String[s-1]=c
if String[0]==0:
    if N!=1:
        flag=0
elif String[0]=='0':
    if N!=1:
        String[0]=1
String=list(map(str,String))
if flag:
    print(int(''.join(String)))
else:
    print(-1)
