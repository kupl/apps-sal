n = int(input())
s = [list(map(int, input().split())) for i in range(n)]
# print(s)
a, b = 0, 100000000000000
for i in s:
    a = max(a, i[0])
    b = min(b, i[1])
ans = 1000000000000
i2, i3 = -1, -1
len1 = 1000000000000000
len2 = 1000000000000000
# print(s)
for i in range(n):
    if s[i][0] == a:
        if len1 > s[i][1] - s[i][0]:
            len1 = s[i][1] - s[i][0]
            i2 = i
    if s[i][1] == b:
        if len2 > s[i][1] - s[i][0]:
            len2 = s[i][1] - s[i][0]
            i3 = i
ans1, ans2 = -1, -1
# print(s)
a, b = -1, 1000000000000000
for k in range(n):
    if k == i2:
        continue
    i = s[k]
    a = max(a, i[0])
    b = min(b, i[1])
ans1 = b - a
a, b = -1, 12000000000000
# print(s)
for k in range(n):
    if k == i3:
        continue
    i = s[k]
    a = max(a, i[0])
    b = min(b, i[1])
ans2 = b - a
#print(ans1, i2)
#print(ans2, i3)
print(max(0, ans1, ans2))
