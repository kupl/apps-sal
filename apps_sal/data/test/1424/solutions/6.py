def dif(x, y):
    c = 0
    while x != 0 or y != 0:
        if x % 2 != y % 2:
            c += 1
        x //= 2
        y //= 2
    return c


n, m, k = map(int, input().split())
x = [int(input()) for i in range(m + 1)]
cnt = 0
for i in range(m):
    if dif(x[i], x[m]) <= k:
        cnt += 1
print(cnt)
