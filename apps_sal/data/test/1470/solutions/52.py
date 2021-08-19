x = int(input())
y = x % 11
if y > 0:
    cnt = 1
    if y > 6:
        cnt += 1
else:
    cnt = 0
print(x // 11 * 2 + cnt)
