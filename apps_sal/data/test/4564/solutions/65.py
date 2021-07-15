S=input()
a=[0]*26
num=ord('a')
for i in range(len(S)):
    tmp=ord(S[i])-num
    if a[tmp]:
        print('no')
        break
    a[tmp]=1
else:
    print('yes')

