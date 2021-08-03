n = int(input())
t = [int(x) for x in input().split()]
cnt = [[0], [0], [0], [0]]
for i in range(n):
    if t[i] == 1:
        cnt[1][0] += 1
        cnt[1].append(i + 1)
    elif t[i] == 2:
        cnt[2][0] += 1
        cnt[2].append(i + 1)
    elif t[i] == 3:
        cnt[3][0] += 1
        cnt[3].append(i + 1)
m = 1000000000000
for i in range(1, len(cnt)):
    m = min(cnt[i][0], m)
print(m)
for j in range(1, m + 1):
    for i in range(1, len(cnt)):
        print(cnt[i][j], end=' ')
    print()
