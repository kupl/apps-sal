N=int(input())
ans=''
while 1:
    ans+=str(N%2)
    if N in [0,1]:
        break
    N=0-N//2
print(ans[::-1])
