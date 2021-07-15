#print('Hare Krishna')
def I():
    return int(input())
def IL():
    return [int(i) for i in input().split()]
def IS():
    return input()
def IM():
    return map(int,input().split())
t=I()
for i in range(t):
    s1=IS()
    s2=IS() 
    f=1 
    if len(s1)>len(s2):
        print('NO')
        continue 
    if len(s1)==len(s2):
        print('YES' if s1==s2 else 'NO')
        continue 
    grps1=[] 
    grps2=[]
    i=0 
    n=len(s1)
    m=len(s2)
    while i<n:
        curr=s1[i]
        c=0 
        while i<n and s1[i]==curr:
            c+=1 
            i+=1 
        grps1.append([curr,c])
    i=0 
    while i<m:
        curr=s2[i]
        c=0 
        while i<m and s2[i]==curr:
            c+=1 
            i+=1 
        grps2.append([curr,c])
    #print(grps1,grps2)
    if len(grps1)!=len(grps2):
        print('NO')
        continue 
    f=1 
    for i in range(len(grps1)):
        if grps1[i][0]!=grps2[i][0] or grps1[i][1]>grps2[i][1]:
            f=0 
    print('YES' if f else 'NO')
