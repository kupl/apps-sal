n = int(input())
(s, t) = map(list, input().split())
ans = []
for i in range(n):
    ans.append(s[i])
    ans.append(t[i])
print(''.join(ans))
