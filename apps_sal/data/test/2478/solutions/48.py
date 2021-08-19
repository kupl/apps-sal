n = int(input())
s = list(input())
d = [0]
x = 0
for i in range(len(s)):
    if s[i] == '(':
        x += 1
    else:
        x -= 1
    d.append(x)
ans = []
x = min(d)
for i in range(max(0, -1 * x)):
    ans.append('(')
for i in s:
    ans.append(i)
for i in range(max(d[len(d) - 1] - x, 0)):
    ans.append(')')
a = ''.join(ans)
print(a)
