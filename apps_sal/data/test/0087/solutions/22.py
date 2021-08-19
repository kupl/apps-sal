days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
(month, first) = map(int, input().split())
first -= 1
cnt = 1
x = days[month - 1] - (7 - first)
cnt += x // 7
if x % 7 != 0:
    cnt += 1
print(cnt)
