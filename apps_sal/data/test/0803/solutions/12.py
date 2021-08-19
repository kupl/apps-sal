n = int(input())
s = list(input())
X = s.count('X')
x = s.count('x')
ans = 0
for i in range(n):
    if X > x and s[i] == 'X':
        s[i] = 'x'
        ans += 1
        X -= 1
        x += 1
    elif X < x and s[i] == 'x':
        s[i] = 'X'
        ans += 1
        X += 1
        x -= 1
print(ans)
for item in s:
    print(item, end='')
