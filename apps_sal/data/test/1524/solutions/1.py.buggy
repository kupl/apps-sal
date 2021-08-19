s = input()
n = len(s)
l = []
i = 0
while i < n:
    j = 1
    while i + j < n and s[i] == s[i + j]:
        j += 1
    l.append((s[i], j, i))
    i += j

ans = [0] * n
i = 0
if l[0][0] == 'L':
    ans[0] = l[0][1]
    i += 1

while i + 1 < len(l):
    cr, R, pr = l[i]
    cl, L, pl = l[i + 1]
    ans[pl - 1] = (R + 1) // 2 + L // 2
    ans[pl] = (L + 1) // 2 + R // 2
    i += 2

if l[-1][0] == 'R':
    ans[-1] = l[-1][1]
print((*ans))
