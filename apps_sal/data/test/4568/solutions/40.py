
N = int(input())
S = input()

ans = 0
for i in range(1,N):
    common = set(S[i:]) & set(S[:i])
    ans = max(ans,len(common))

print(ans)
