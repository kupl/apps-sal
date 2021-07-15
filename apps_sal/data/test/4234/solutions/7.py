n = int(input())
use = [True for i in range(n)]
s = input()
now = 0
flag = 0
for i in range(1, n):
    if flag == 1:
        flag = 0
        continue
    if s[now] == s[i]:
        use[i] = False
    else:
        flag = 1
        now = i+1
ans = ""
for i in range(n):
    if use[i]:
        ans += s[i]
if len(ans) % 2 == 1:
    ans = ans[:-1]

print(n-len(ans))
print(ans)

