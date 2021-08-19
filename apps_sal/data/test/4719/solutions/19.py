n = int(input())
S = [input() for _ in range(n)]
C = [[0] * 26 for _ in range(n)]
for i in range(n):
    for x in S[i]:
        k = ord(x) - ord('a')
        C[i][k] += 1
count = C[0]
for i in range(1, n):
    for k in range(26):
        count[k] = min(count[k], C[i][k])
ans = []
for k in range(26):
    if count[k]:
        ans.append(chr(ord('a') + k) * count[k])
print(*ans, sep='')
