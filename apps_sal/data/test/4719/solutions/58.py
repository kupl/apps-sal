N = int(input())
INF = 10 ** 12
ans = [INF] * 26
for _ in range(N):
    S = input()
    tmp = [0] * 26
    for s in S:
        tmp[ord(s) - ord('a')] += 1
    for i in range(26):
        ans[i] = min(ans[i], tmp[i])
ansS = ''
for i in range(26):
    ansS += chr(i + 97) * ans[i]
print(ansS)
