n = int(input())
ans = 0
n %= 360

if n <= 45 or n >= 270:
    ans = 0
if n > 45 and n <= 135:
    ans = 1
if n > 135 and n <= 225:
    ans = 2
if n > 225 and n < 315:
    ans = 3
print(ans)

