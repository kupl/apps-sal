(n, k) = list(map(int, input().split()))
s = list(input())
ans = False
for i in range(len(s) - k + 1):
    flag = True
    for j in range(i, i + k):
        if s[j] == 'Y':
            flag = False
            break
    if i + k < len(s) and s[i + k] == 'N':
        flag = False
    if i > 0 and s[i - 1] == 'N':
        flag = False
    if flag:
        ans = True
        break
maximum = 0
i = 0
while i < len(s):
    now = 0
    while s[i] != 'N':
        i += 1
        if i >= len(s):
            break
    if i >= len(s):
        break
    while i < len(s) and s[i] == 'N':
        i += 1
        now += 1
    maximum = max(maximum, now)
if ans and maximum <= k:
    print('YES')
else:
    print('NO')
