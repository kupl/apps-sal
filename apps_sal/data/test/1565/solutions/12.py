n = int(input())
s = input()
al_l = []
al_r = []
for i in range(1, n):
    if int(s[i]) > 0 and i <= n // 2:
        al_l.append(i)
    if int(s[i]) > 0 and i > n // 2:
        al_r.append(i)
    if len(al_r) == 3:
        break
    if len(al_l) == 3:
        del al_l[0]
ans = int(s)
for x in al_l:
    ans = min(ans, int(s[0:x]) + int(s[x:]))
for x in al_r:
    ans = min(ans, int(s[0:x]) + int(s[x:]))
print(ans)
