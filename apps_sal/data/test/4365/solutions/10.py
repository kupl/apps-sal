K = int(input())

cnt = 0
for i in range(K, 1, -1):
    for _ in range(i - 1, 0, -2):
        cnt += 1
print(cnt)
