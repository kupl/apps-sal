N = int(input())

yakusuu8_cnt = 0
for i in range(1, N + 1):
    if i % 2 == 1:
        yakusuu_cnt = 0
        for j in range(1, i + 1):
            if i % j == 0:
                yakusuu_cnt += 1
            if yakusuu_cnt == 8:
                yakusuu8_cnt += 1

print(yakusuu8_cnt)
