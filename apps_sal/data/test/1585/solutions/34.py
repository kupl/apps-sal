x, y = list(map(int, input().split()))
cnt = 1
while 1:
    if x * 2 <= y:
        cnt += 1
        x *= 2
    else:
        break
print(cnt)
