s = input().split(' ')
n = int(s[0])
m = int(s[1])
ans = -1
up = n
down = 0
left = m
right = 0
have = 0
for i in range(n):
    s = input()
    for j in range(m):
        if s[j] == 'B':
            have += 1
            up = min(up, i)
            down = max(down, i)
            left = min(left, j)
            right = max(right, j)

if have == 0:
    print(1)
else:
    if up <= down and left <= right:
        l = max(down - up + 1, right - left + 1)
        if l <= min(n, m):
            print(l * l - have)
        else:
            print(-1)
