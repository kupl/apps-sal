n=int(input())
s=input()
s2=[]
for i in range(n):
    s2.append(s[i])
    while len(s2) > 2:
        if s2[-1] == 'x' and s2[-2]=='o' and s2[-3] == 'f':
            s2.pop()
            s2.pop()
            s2.pop()
        else:
            break
while len(s2) > 2:
        if s2[-1] == 'x' and s2[-2]=='o' and s2[-3] == 'f':
            s2.pop()
            s2.pop()
            s2.pop()
        else:
            break
print(len(s2))
