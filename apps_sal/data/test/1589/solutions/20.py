(n, m) = list(map(int, input().split()))
ans = 0
for i in range(n):
    flats = list(map(int, input().split()))
    f = [False for i in range(m)]
    for j in range(m * 2):
        f[j // 2] |= True if flats[j] == 1 else False
    ans += f.count(True)
print(ans)
