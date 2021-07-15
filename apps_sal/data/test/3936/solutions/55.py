n = int(input())
s1 = input()
s2 = input()

mod = 10**9+7
yoko = True
if s1[0]==s2[0]:
    ans = 3
    cur = 1
    yoko = False
else:
    ans = 6
    cur = 2

while cur<n:
    if s1[cur]==s2[cur]:
        ans *= 1 if yoko else 2
        ans %= mod
        cur += 1
        yoko = False
    else:
        ans *= 3 if yoko else 2
        ans %= mod
        cur += 2
        yoko = True

print(ans)
