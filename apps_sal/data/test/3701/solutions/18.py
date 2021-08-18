n, x, y = list(map(int, input().split()))
line = input()
temp = line.split('1')
cnt = 0
for i in temp:
    if len(i) > 0:
        cnt += 1
print(min(y * cnt, abs(y + x * (cnt - 1))))
