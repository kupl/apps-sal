from math import ceil
x = int(input())
ans = x // 11
x -= ans * 11
ans *= 2
if x > 0:
    if x <= 6:
        ans += 1
    else:
        ans += 2
print(ans)
