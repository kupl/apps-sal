N = int(input())
s = []
for i in range(N):
    s.append(input())
s.append('')
M = int(input())
t = []
for j in range(M):
    t.append(input())

ans = 0
for i in range(N + 1):
    target = s[i]
    cnt = 0
    for j in range(N):
        if target == s[j]:
            cnt += 1
    for k in range(M):
        if target == t[k]:
            cnt -= 1
    ans = max(ans, cnt)
print(ans)

