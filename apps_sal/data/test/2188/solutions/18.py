from sys import stdin
n=int(stdin.readline().strip())

s=[list(map(int,stdin.readline().strip().split())) for i in range(n)]
s1=[]
s2=[]
for i in range(n):
    if s[i][0]>s[i][1]:
        s1.append(s[i][::-1]+[i])
    if s[i][0]<s[i][1]:
        s2.append(s[i][::-1]+[i])
s1.sort()
s2.sort(reverse=True)
ans1=[]
ans2=[]
if len(s1)>0:
    ans1=[s1[0]]
if len(s2)>0:
    ans2=[s2[0]]
for i in range(len(s1)):
    if ans1[-1][0]<s1[i][0]:
        ans1.append(s1[i])
for i in range(len(s2)):
    if ans2[-1][0]>s2[i][0]:
        ans2.append(s2[i])
if len(ans1)>len(ans2):
    r=[]
    for i in ans1:
        r.append(i[2]+1)
    print(len(r))
    print(*r)
else:
    r=[]
    for i in ans2:
        r.append(i[2]+1)
    print(len(r))
    print(*r)

