(num, n) = map(int, input().split())
a = []
b = []
center = ''
for i in range(num):
    s = input()
    if s[::-1] == s:
        center = s
    if s[::-1] in a:
        b.append(s)
    else:
        a.append(s)
ans = ''
for x in b:
    ans += x
ans = ans + center + ans[::-1]
print(len(ans))
print(ans)
