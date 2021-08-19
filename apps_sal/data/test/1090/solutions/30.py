n, k = map(int, input().split())
s = input()
edge, inside, cnt, ix = 0, 0, 0, 0
if s[0] == 'R' or s[-1] == 'R':
    edge += 1
temp = ''
# print(ix)
s += 'L'
for i in range(n + 1):
    if i != n:
        if temp == 'R' and s[i] == 'L':
            inside += 1
        elif temp == s[i]:
            cnt += 1
    temp = s[i]
# print(inside,cnt,edge)
if inside >= k:
    print(min(k * 2 + cnt, n - 1))
else:
    print(min(inside * 2 + edge + cnt, n - 1))
