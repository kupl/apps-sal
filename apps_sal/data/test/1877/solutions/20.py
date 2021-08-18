
n = int(input())
s = input()
x = 0
y = 0
cnt = 0
for i in range(n):
    if s[i] == "U":
        y += 1
    else:
        x += 1
    if x == y and i + 1 < n:
        if (s[i] == 'U' and s[i + 1] == 'U') or (s[i] == 'R' and s[i + 1] == 'R'):
            cnt += 1
print(cnt)
