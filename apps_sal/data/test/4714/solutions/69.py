a, b = map(int, input().split())

cnt = 0
for i in range(1, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            num = int(str(i) + str(j) + str(k) + str(j) + str(i))
            if a <= num <= b:
                cnt += 1

print(cnt)
