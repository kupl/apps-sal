n, k = map(int, input().split())
s = input()
ss = []
ss.append(0)
for i in range(n - 1):
    a = s[i]
    if a == s[i + 1]:
        continue
    ss.append(i + 1)
ss.append(n)

ans = 0
for i in range(len(ss)):
    p = ss[i]
    if p == n:
        break
    if s[p] == "0":
        ans = max(ans, ss[min(2 * k + i, len(ss) - 1)] - ss[i])
    else:
        ans = max(ans, ss[min(2 * k + 1 + i, len(ss) - 1)] - ss[i])
print(ans)
