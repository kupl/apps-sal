x = int(input())
cnt = 0
cnt += x // 11 * 2
if 0 < x % 11 <= 6:
    cnt += 1
elif 6 < x % 11 < 11:
    cnt += 2
print(cnt)
