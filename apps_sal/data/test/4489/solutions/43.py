n = int(input())
s = [input() for i in range(n)]
m = int(input())
t = [input() for i in range(m)]
ans = []
for i in s:
    cnt = 0
    for j in range(n):
        if i == s[j]:
            cnt += 1
    for k in range(m):
        if i == t[k]:
            cnt -= 1
    ans.append(cnt)
if max(ans) < 0:
    print('0')
else:
    print(max(ans))
