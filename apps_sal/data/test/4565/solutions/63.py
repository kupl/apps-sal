N = int(input())
S = input()

west = [0]*N
east = [0]*N

tmp = 0
for i in range(1,N):
    if S[i-1] == 'W':
        tmp += 1
        west[i] = tmp
    else:
        west[i] = tmp

tmp = 0
for i in range(N-2,-1,-1):
    if S[i+1] == 'E':
        tmp += 1
        east[i] = tmp
    else:
        east[i] = tmp

ans = float('inf')
for i in range(N):
    ans = min(ans,west[i]+east[i])
print (ans)

