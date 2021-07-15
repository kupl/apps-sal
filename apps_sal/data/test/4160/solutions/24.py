X = int(input())
cur = 100
cnt = 0
while cur < X:
    cur = cur * 101 // 100
    cnt += 1
print(cnt)

