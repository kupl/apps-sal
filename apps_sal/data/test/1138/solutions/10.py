s = input()
x = 0
y = 0
for i in range(len(s)):
    if s[i] == 'R':
        x += 1
    if s[i] == 'L':
        x -= 1
    if s[i] == 'U':
        y += 1
    if s[i] == 'D':
        y -= 1
if abs(x) % 2 == 1 and abs(y) % 2 == 1:
    print(abs(x) // 2 + abs(y) // 2 + 1)
elif abs(x) % 2 == 1:
    print(-1)
elif abs(y) % 2 == 1:
    print(-1)
else:
    print(abs(x) // 2 + abs(y) // 2)
