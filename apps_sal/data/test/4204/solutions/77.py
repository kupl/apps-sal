S = list(map(int, input()))
K = int(input())
flag = False
ans = 1
for i in range(K):
    if S[i] != 1:
        flag = True
        ans = S[i]
        break
print(ans)
