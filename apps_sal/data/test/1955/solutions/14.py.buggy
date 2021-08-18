def R(): return map(int, input().split())


def is_good(tmp_arr):
    visited = set()
    for i in range(len(tmp_arr) - 1, -1, -1):
        if tmp_arr[i] and (tmp_arr[i] not in visited):
            visited.add(tmp_arr[i])
            tmp_arr[i] = cost[tmp_arr[i] - 1]
        else:
            tmp_arr[i] = 0
    if len(visited) != m:
        return False
    tot = 0
    for x in tmp_arr:
        tot += (1 if not x else 0) - x
        if tot < 0:
            return False
    return True


n, m = R()
arr = list(R())
cost = list(R())
if not is_good(arr[:]):
    print(-1)
    return
l, r = 0, n - 1
while l < r:
    mid = (l + r) // 2
    if is_good(arr[:mid + 1]):
        r = mid
    else:
        l = mid + 1
print(r + 1)
