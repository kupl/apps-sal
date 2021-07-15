X = int(input())
cnt = 0
dist = 0
while dist < X:
    cnt += 1
    dist += cnt
print(cnt)
