cnt = {}
for i in range(22):
    cnt[i] = {}

# print(cnt)

n, m, k = list(map(int, input().split()))
arr = [list(map(int, input().split())) for i in range(n)]


def check(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    else:
        return True


def go(x, y, now):
    if check(x, y) == False:
        return

    now ^= arr[x][y]
    if x + y == m - 1:
        # print('yes')
        if now in cnt[x]:
            cnt[x][now] += 1
        else:
            cnt[x][now] = 1
        return

    go(x + 1, y, now)
    go(x, y + 1, now)


ans = 0


def goRev(x, y, now):
    if check(x, y) == False:
        return

    if x + y == m - 1:
        cur = k ^ now
        if cur in cnt[x]:
            nonlocal ans
            # print(ans)
            ans += cnt[x][cur]
        return

    now ^= arr[x][y]
    goRev(x - 1, y, now)
    goRev(x, y - 1, now)


go(0, 0, 0)
goRev(n - 1, m - 1, 0)

print(ans)
