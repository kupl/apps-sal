(n, m) = map(int, input().split())
k = [list(map(int, input().split())) for _ in range(n)]
l = [0 for i in range(m)]
count = 0
for i in k:
    for j in i[1:]:
        l[j - 1] += 1
for i in l:
    if i == n:
        count += 1
print(count)
