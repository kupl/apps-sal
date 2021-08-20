from sys import stdin
n = int(stdin.readline().strip())
s = stdin.readline().strip()
ans = 101
for i in range(0, 101):
    x = i
    for j in range(n):
        if s[j] == '-':
            x -= 1
        else:
            x += 1
        if x < 0:
            x = 101
            break
    ans = min(x, ans)
print(ans)
