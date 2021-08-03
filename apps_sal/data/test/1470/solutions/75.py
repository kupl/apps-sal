x = int(input())
c = x // 11
m = x % 11
cnt = 2 * c
if 0 < m < 7:
    cnt += 1
elif 6 < m:
    cnt += 2
print(cnt)
