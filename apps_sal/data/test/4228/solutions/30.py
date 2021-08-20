(n, l) = map(int, input().split())
ans = 0
mv = 100000
for i in range(1, n + 1):
    tmp = l + i - 1
    ans += tmp
    if abs(mv) > abs(tmp):
        mv = tmp
print(ans - mv)
