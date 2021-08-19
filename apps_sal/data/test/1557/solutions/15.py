import sys
(h1, a1, c1) = map(int, input().split())
(h2, a2) = map(int, input().split())
ans = []
while h2 > 0:
    if h1 - a2 <= 0 and h2 - a1 > 0:
        ans.append('HEAL')
        h1 += c1
    else:
        ans.append('STRIKE')
        h2 -= a1
    h1 -= a2
print(len(ans))
for i in range(len(ans)):
    print(ans[i])
