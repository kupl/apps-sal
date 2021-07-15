a, b = map(int, input().split())

cnt = 0
for i in range(a, b+1, 1):
    i = str(i)
    if i[0] == i[4] and i[1] == i[3]:
        cnt += 1
    else:
        continue

print(cnt)
