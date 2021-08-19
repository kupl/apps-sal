(n, k) = map(int, input().split())
s = input()
pre = s[0]
rs = s[0]
first = s[0]
if s[0] == 'R':
    second = 'L'
else:
    second = 'R'
for i in s[1:]:
    if i == second and k > 0:
        rs = rs + first
        pre = i
    elif i == first and pre == second:
        k -= 1
        rs = rs + i
        pre = i
    elif k == 0:
        rs = rs + i
    elif i == first and pre == first:
        rs = rs + i
pre = '0'
ans = 0
for i in rs:
    if i == pre:
        ans += 1
    pre = i
print(ans)
