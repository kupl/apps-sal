a, b = map(int, input().split())
cnt = 0
for i in range(1, 64):
    k = (1 << i) - 1
    for j in range(0, i - 1):
        num = k - (1 << j)
        if (a <= num and num <= b):
            cnt += 1
print(cnt)
