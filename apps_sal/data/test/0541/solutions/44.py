n, m = map(int, input().split())
lst = [list(map(int, input().split())) for i in range(m)]
lst.sort(key=lambda x: x[1])
ans = 1
pin = lst[0][1] - 1

for i in range(1, m):
    if lst[i][0] > pin:
        ans += 1
        pin = lst[i][1] - 1

print(ans)
