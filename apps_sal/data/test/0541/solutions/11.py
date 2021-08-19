(N, M) = map(int, input().split())
li = []
for i in range(M):
    (a, b) = map(int, input().split())
    li.append([b, a])
li.sort()
an = 1
now_end = li[0][0]
for i in range(1, M):
    if now_end <= li[i][1]:
        an += 1
        now_end = li[i][0]
print(an)
