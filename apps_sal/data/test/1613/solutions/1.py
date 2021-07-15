n = int(input())
k = [[0, 0, -1]]
cnt = 0
for i in map(int, input().split()):
    if i:
        if k[-1][0] == i:
            k[-1][1] += 1
        else:
            k.append([i, 1, cnt])
    cnt += 1
cnt = 0
ans = 0
for i in k[1:]:
    ans += min(i[1], i[2] - cnt)
    cnt += i[1]
print(ans)
