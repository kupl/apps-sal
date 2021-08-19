(n, m) = map(int, input().split())
pair = []
own = []
mentu = []
for _ in range(n):
    s = list(input())
    if s == s[::-1]:
        own.append(s)
    elif s[::-1] in mentu:
        pair.append(s)
    else:
        mentu.append(s)
k = 1 if own else 0
print(k * m + len(pair) * 2 * m)
ans = ''
for s in pair:
    ans += ''.join(s)
if own:
    for s in own[0]:
        ans += ''.join(s)
for s in pair[::-1]:
    ans += ''.join(s[::-1])
print(ans)
