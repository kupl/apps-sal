n = int(input())
s = list(str(input()))
x = 0
y = 0
for i in range(n):
    if s[i] == '(':
        x += 1
    if s[i] == ')':
        if x >= 1:
            x -= 1
        else:
            y += 1
for _ in range(x):
    s.append(')')
for _ in range(y):
    s.insert(0, '(')
ans = ''.join(s)
print(ans)
