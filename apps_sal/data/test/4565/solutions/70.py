N = int(input())
S = input()
west = S.count('W')
east = N - west 
Q = [0,0,west,east] #[自分より西で西向き、東向き、自分より東で西向き、東向き]
ans = N-1
for i in range(N):
    if S[i]=='W':
        Q[2]-=1
        cnt = Q[0]+Q[3]
        Q[0]+=1
    else:
        Q[3]-=1
        cnt = Q[0]+Q[3]
        Q[1]+=1
    ans = min(ans,cnt)
print(ans)
