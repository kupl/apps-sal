n = int(input())
used = [False for i in range(n + 2)]
arr = list(map(int, input().split()))
cnt = 0
maxx = 0
for i in range(2 * n):
    if used[arr[i]]:
        cnt -= 1
        used[arr[i]] = False
    else:
        used[arr[i]] = True
        cnt += 1
        maxx = max(maxx, cnt)
print(maxx)
