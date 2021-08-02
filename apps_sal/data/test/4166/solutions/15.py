N, M = map(int, input().split())
s = [0] * M
c = [0] * M
d = dict()
for i in range(M):
    s[i], c[i] = map(int, input().split())
    if s[i] in d:
        if d[s[i]] != c[i]:
            ans = -1
            break
    else:
        d[s[i]] = c[i]
else:
    ans = ""
    for i in range(1, N + 1):
        if i in d:
            ans += str(d[i])
        else:
            if i >= 2 and ans != "" and ans[0] == "0":
                ans = -1
                break
            elif N >= 2 and i == 1:
                ans += str(1)
            else:
                ans += str(0)

print(ans)
