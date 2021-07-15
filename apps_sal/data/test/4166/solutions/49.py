N,M=map(int,input().split())
X=['*','*','*']
for i in range(M):
  s,c=map(str,input().split())
  for j in range(M):
    if s=='1' and X[0]=='*':X[0]=c;continue
    elif s=='1' and c!=X[0]:print(-1);return
    if s=='2' and X[1]=='*':X[1]=c;continue
    elif s=='2' and c!=X[1]:print(-1);return
    if s=='3' and X[2]=='*':X[2]=c;continue
    elif s=='3' and c!=X[2]:print(-1);return
if N==1 and X[0]=='*':print('0');return
if N==1:print(X[0]);return
if X[0]=='0':print(-1);return
if X[0]=='*':X[0]='1'
if X[1]=='*':X[1]='0'
if N==2:print(int(X[0])*10+int(X[1]));return
if X[2]=='*':X[2]='0'
print(int(X[0])*10**2+int(X[1])*10+int(X[2]))
