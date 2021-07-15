n = int(input())
arr = list(map(int, input().split()))
used = [0 for i in range(n)]
cur = 0
maxn = -1
for i in range(2 * n):
    if used[arr[i] - 1] == 0:
        cur += 1
        used[arr[i] - 1] = 1
    else:
        used[arr[i] - 1] -= 1
        cur -= 1
    maxn = max(maxn, cur)
print(maxn)
