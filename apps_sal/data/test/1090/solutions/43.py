n,k = list(map(int, input().split()))
S = input()

ans = []
c = 1
# RL圧縮
for i in range(1,n):
    if S[i-1] == S[i]:
        c += 1
    else:
        ans.append(c)
        c = 1
ans.append(c)
# ansの個数は1個毎に減っていく
if len(ans) // 2  <= k:
    print((n-1))
else:
    d = len(ans) - 2*k
    print((n-d))

