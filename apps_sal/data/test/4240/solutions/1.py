import sys
S = input().strip()
T = input().strip()
ans = 'No'
for _ in range(len(S)):
    S = S[-1] + S[:-1]
    if S == T:
        ans = 'Yes'
print(ans)
