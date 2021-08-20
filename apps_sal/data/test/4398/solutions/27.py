n = int(input())
(s, t) = input().split(' ')
ans = []
for i in range(n):
    ans.append(s[i] + t[i])
for i in range(n):
    print(ans[i], end='')
print()
