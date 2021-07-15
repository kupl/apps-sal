n = int(input())
s = input()
k = 0
l = []
for i in range(len(s)-1):
    if(s[i]<=s[i+1]):
        k+=1
    else:
        l.append([i+1,i+2])
if(k==len(s)-1):
    print('NO')
else:
    print('YES')
    print(*l[0])

