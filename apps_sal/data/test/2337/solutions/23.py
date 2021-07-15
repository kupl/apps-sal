n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

j = -1

cnt = 0

for v in a:
    j += 1
    while j < m and v > b[j]:
        j += 1

    if j >= m:
        cnt += 1

print(cnt)
