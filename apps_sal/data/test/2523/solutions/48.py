s = input()
L = len(s)

l, r, p = 0, 0, s[L // 2]
if L % 2 == 0:
    l, r = L // 2 - 1, L // 2
else:
    l, r = L // 2, L // 2

cnt = 0
while l >= 0 and r < L and s[l] == s[r] == p:
    p = s[l]
    cnt += 1
    l -= 1
    r += 1

print((cnt + L // 2))

