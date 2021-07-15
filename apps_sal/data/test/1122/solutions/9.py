N,M = map(int,input().split())
ans = []
if N%2:
    for i in range(N//2):
        ans.append((i+1, N-1-i))
else:
    m = N//2
    for i in range(m//2):
        ans.append((i+1, m-i))
    for i in range((m-1)//2):
        ans.append((m+i+1, N-1-i))
for a,b in ans[:M]:
    print(a,b)
