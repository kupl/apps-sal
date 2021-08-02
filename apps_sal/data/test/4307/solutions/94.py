n = int(input())
score = []
for s in range(1, n + 1, 2):
    count = 0
    for t in range(1, s + 1):
        if (s % t == 0):
            count += 1
    score.append(count)
cnt = 0
for i in score:
    if (i == 8):
        cnt += 1
print(cnt)
