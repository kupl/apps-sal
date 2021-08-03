x, y = list(map(int, input().split()))
cnt = 0
while x <= y:
    x = x * 2
    cnt += 1
print(cnt)
