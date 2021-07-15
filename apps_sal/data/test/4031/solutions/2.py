n = int(input())
ans = []
s = [input() for i in range(n)]
for i in range(n):
    for j in range(len(s)):
        t = True
        for k in range(len(s)):
            if j == k:
                continue
            if s[j] not in s[k]:
                t = False
                break
        if t:
            ans.append(s[j])
            del s[j]
            break
if len(ans) == n:
    print('YES')
    for i in ans:
        print(i)
else:
    print('NO')

