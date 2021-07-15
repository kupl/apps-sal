n,k=[int(x) for x in input().split()]
if n<k or (k==1 and n>=2):
    print(-1)
    return
if k==1:
    print('a')
    return
st=""
flag=1
for i in range(n-k+2):
    if flag:
        st+='a'
        flag=0
    else:
        st+='b'
        flag=1
num=ord('c')
for i in range(0,k-2):
    st+=chr(num+i)
print(st)
    

