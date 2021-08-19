k = int(input())
cnt = 0
for i in range(1, k + 1):
    for j in range(2, k + 1):
        if i % 2 == 1 and j % 2 == 0:
            cnt += 1
print(cnt)
