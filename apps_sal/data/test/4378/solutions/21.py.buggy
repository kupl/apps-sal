n = int(input())
s = input()
c = 'RGB'
ans = ''
ansk = 0
flag = True

for i in range(n - 1):
    if flag:
        if s[i] == s[i + 1]:
            if i == n - 2:
                ans += s[i] + c[c.find(s[i]) - 1]
                ansk += 1
                print(ansk)
                print(ans)
                return
            else:
                for j in c:
                    if j != s[i] and j != s[i + 2]:
                        break
                flag = False
                ansk += 1
                ans += s[i] + j
        else:
            ans += s[i]
    else:
        flag = True

print(ansk)
print(ans + s[-1])
