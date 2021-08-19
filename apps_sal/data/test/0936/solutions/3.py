n = int(input())
a = map(int, input().split())
s = dict()
ans = -1
pos = 1
for i in a:
    if i in s:
        s[i] += 1
    else:
        s[i] = 1
    if ans < s[i]:
        (pos, ans) = (i, s[i])
print(pos)
