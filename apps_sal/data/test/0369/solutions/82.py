(N, M) = map(int, input().split())
S = input()
ans = []
i = N
while i > 0:
    prev = i
    for j in range(max(0, i - M), i):
        if S[j] == '0':
            ans.append(str(i - j))
            i = j
            break
    if i == prev:
        ans = -1
        break
if ans == -1:
    print(ans)
else:
    ans.reverse()
    print(*ans)
