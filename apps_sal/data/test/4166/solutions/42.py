N, M = list(map(int, input().split()))
s, c = [None] * M, [None] * M
for i in range(M):
    s[i], c[i] = list(map(int, input().split()))


ans = 0
l = [None] * N
for i in range(M):
    if l[s[i] - 1] == None:
        l[s[i] - 1] = c[i]

if N == 1 and l[0] == None:
    l[0] = 0
elif N > 1 and l[0] == None:
    l[0] = 1
for i in range(1, N):
    if l[i] == None:
        l[i] = 0

if N > 1 and l[0] == 0:
    ans = -1
else:
    for i in range(M):
        for j in range(i + 1, M):
            if s[i] == s[j] and c[i] != c[j]:
                ans = -1
                break
    if ans != -1:
        l = list(map(str, l))
        ans = "".join(l)
print(ans)
