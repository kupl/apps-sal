n = int(input())
s = [input() for _ in range(n)]
ans = set(s[0])
for i in range(1, n):
    ans = ans & set(s[i])
cnt = [0] * len(ans)
ans = sorted(list(ans))
for i in range(n):
    for j in range(len(ans)):
        if cnt[j] == 0:
            cnt[j] = s[i].count(ans[j])
        else:
            cnt[j] = min(cnt[j], s[i].count(ans[j]))

A = ""
for x, y in zip(ans, cnt):
    A += x * y
print(A)
