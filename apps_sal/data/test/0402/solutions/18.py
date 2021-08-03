n, k = list(map(int, input().split()))
res = 0
cur = 60 * 4
for i in range(1, n + 1):
    if cur - 5 * i >= k:
        res += 1
        cur -= 5 * i
    else:
        break
print(res)
