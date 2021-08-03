N, M = map(int, input().split())
S = input()

ans = []
i = N
while i > 0:
    if i <= M:
        ans.append(i)
        break
    for j in range(M, 0, -1):
        if S[i - j] == '1':
            continue
        ans.append(j)
        i -= j
        break
    else:
        print(-1)
        return
print(*ans[::-1])
