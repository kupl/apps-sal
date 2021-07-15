n=input()

ans=[]
for i in n:
    if i=='1':
        ans.append('9')
    else:
        ans.append('1')

print(''.join(ans))
