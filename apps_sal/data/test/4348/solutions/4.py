(n, k) = [int(i) for i in input().split()]
s = [0 for i in range(26)]
t = ''
for i in input():
    t += i
    s[ord(i) - 97] += 1
kar = 0
kol = 0
for i in range(len(s)):
    if k > s[i]:
        kar += 1
        k -= s[i]
    else:
        kol = k
        break
ans = ''
for i in range(n):
    if ord(t[i]) - 97 == kar and kol > 0:
        kol -= 1
    elif ord(t[i]) - 97 == kar:
        ans += t[i]
    if ord(t[i]) - 97 > kar:
        ans += t[i]
print(ans)
