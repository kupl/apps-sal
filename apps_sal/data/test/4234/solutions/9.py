n = int(input())
s = input()
ans = ''
v = [0] * n
flag = True
for i in range(n - 1):
    if flag:
        if s[i] == s[i + 1]:
            v[i] = 1
        else:
            flag = False
    else:
        flag = not flag
for i in range(n):
    if v[i] == 0:
        ans += s[i]
if len(ans) % 2:
    ans = ans[:-1]
print(n - len(ans))
print(ans)
