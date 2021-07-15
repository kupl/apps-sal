N=int(input())
S=input()
cnt=0
for i in range(N):
    left=i-1
    right=i+1
    while 0<=left and right<N:
        if S[i]!=S[left] and S[i]!=S[right] and S[left]!=S[right]:
            cnt+=1
        left-=1
        right+=1
x=S.count('R')
y=S.count('G')
z=S.count('B')
print((x*y*z-cnt))

