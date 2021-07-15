n, k = map(int, input().split())
s = input()
pre = s[0]
ans = s[0]
first = s[0]

if s[0] == "R":
    second = "L"
else:
    second = "R"

for i in s[1:]:
    if i == second and k > 0:
        ans = ans + first
        pre = i
    elif i == first and pre == second:
        k -= 1
        ans = ans + i
        pre = i
    elif k == 0:
        ans = ans + i
    elif i == first and pre == first:
        ans = ans + i

pre = "0"
cnt = 0

for i in ans:
    if i == pre:
        cnt += 1
    pre = i

print(cnt)
