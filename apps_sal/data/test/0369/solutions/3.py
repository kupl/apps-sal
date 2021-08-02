import sys
N, M = map(int, input().split())
S = input()
S = S[::-1]
i = 0
ans = []
while i < N:
    flag = 0
    for j in range(M, 0, -1):
        if i + j <= N and S[i + j] == '0':
            i += j
            flag = 1
            ans.append(j)
            break
    if flag:
        continue
    print(-1)
    return
ans.reverse()
print(*ans)
