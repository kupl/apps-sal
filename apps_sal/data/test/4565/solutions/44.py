N = int(input())
S = list(input())
allW = S.count('W')
allE = S.count('E')
numW = S.count('E')
numE = 0
ans = 3*10**5
for i in range(N):
    if S[i] == 'E':
        numW -= 1
    ans = min(ans,numW + numE)
    if S[i] == 'W':
        numE += 1   
print(ans)
