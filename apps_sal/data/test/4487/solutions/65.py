s = (input().split())
t = len(s)
cnt = 0
for i in range(t):
    if i != t - 1:
        if (s[i][-1]) == s[i + 1][0]:
            cnt += 1
    else:
        break

if cnt == t - 1:
    print("YES")
else:
    print("NO")
