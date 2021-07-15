w=input()
l=[0 for _ in range(26)]
Flag=True
for i in w:
    num=ord(i)-97
    #print(num)
    l[num]+=1
for i in l:
    if i%2==1:
        Flag=False
if Flag:
    print('Yes')
else:
    print('No')

