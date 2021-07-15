n, k = map(int, input().split())

ans = 0
for i in range(1, n + 1):
    j = i
    cnt = 1
    while j < k:
        j <<= 1
        cnt /= 2
    ans += cnt / n
print('{:10}'.format(ans))
