import sys
n = int(input())
s = input()
a = []
for i in range(n):
    if s[i] == 'L':
        a.append(['L', i])
    if s[i] == 'R':
        a.append(['R', i])
i = 0
j = len(a) - 1

if len(a) == 0:
    print(n)
    return
if a[0][0] == 'L':
    A = a[0][1]
    i = 1
else:
    A = -1
if a[len(a) - 1][0] == 'R':
    j = len(a) - 2
    D = a[-1][1]
else:
    D = n
ans = 0
if i > j:
    B  = 1
    C = 0
else:
    B = a[i][1]
    C = a[j][1]
while i < j:
    if (a[i][1] - a[i + 1][1]) % 2 == 0:
        ans += 1
    if i != j - 1:
        ans += (a[i + 2][1] - a[i + 1][1] - 1)
    i += 2
if B > C:
    ans += (D - A - 1)
else:
    ans += (B - A - 1 + D - C - 1)
print(ans)
