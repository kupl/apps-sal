s = input()
t = input()
ans = 10 ** 5
n = len(s)
for i in range(n - len(t) + 1):
    cnt = 0
    for j in range(len(t)):
        if s[i + j] != t[j]:
            cnt += 1
    ans = min(ans, cnt)

print(ans)
