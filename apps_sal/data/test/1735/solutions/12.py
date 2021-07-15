s = input()
lis = []
cnt = 0
for c in s:
    lis.append(c)
    if len(lis)>1:
        if lis[-1]==lis[-2]:
            lis.pop()
            lis.pop()
            cnt = cnt+1
if cnt%2==0:
    print('No')
else:
    print('Yes')

