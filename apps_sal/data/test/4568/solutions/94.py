N = int(input())
S = input()
ans = 0
for i in range(N):
    X = S[0:i]
    Y = S[i:N]
    XY = set(X) & set(Y)
    cnt = len(XY)
    ans = max(ans, cnt)
print(ans)
