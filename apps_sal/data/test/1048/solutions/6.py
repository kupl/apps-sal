n = int(input())
s = input()
x = 0
y = 0
for i in range(n):
    if s[i] == 'U':
        y += 1
    if s[i] == 'D':
        y -= 1
    if s[i] == 'L':
        x -= 1
    if s[i] == 'R':
        x += 1
ans = n - abs(x) - abs(y)
print(max(0, ans))
