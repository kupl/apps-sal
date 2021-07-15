import sys
n = int(input())
s = str(input())
ans = num = 0
l = r = False
k = 0
j = 0
while j < n:
    if s[j] == 'R' or s[j] == 'L':
        break
    else:
        j += 1
if j == n:
    print(n)
    return
for i in range(n):
    if s[i] == '.' and l is False:
        num += 1

    if s[i] == 'L' and r is False:
        num = 0
        l = True
    if s[i] == '.' and l is True:
        ans += 1
    if s[i] == 'R' and l is True:
        k = i
        l = False
        r = True
    if s[i] == 'R' and l is False:
        ans += num
        num = 0
        r = True
    if s[i] == 'L' and r is True:
        if num % 2 == 1:
            ans += 1
        num = 0
        l = True
        f = False

print(ans)
