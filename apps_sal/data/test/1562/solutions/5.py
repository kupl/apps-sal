(n, m, k, q) = map(int, input().split())
tr_min = [None for _ in range(n)]
tr_max = [None for _ in range(n)]
for _ in range(k):
    (row, col) = map(int, input().split())
    row = n - row
    col -= 1
    if tr_min[row] == None or col < tr_min[row]:
        tr_min[row] = col
    if tr_max[row] == None or col > tr_max[row]:
        tr_max[row] = col
tr_min[-1] = 0
tr_max[-1] = tr_max[-1] or 0
savecols = sorted(map(lambda t: int(t) - 1, input().split()))


def binsearch(arr, val):
    (l, r) = (0, len(arr) - 1)
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] < val:
            l = mid + 1
        elif arr[mid] > val:
            r = mid - 1
        else:
            return mid
    return r


def find_short_descent(A, B):
    if A > B:
        return find_short_descent(B, A)
    idx1 = binsearch(savecols, A)
    idx2 = idx1 + 1
    minval = m * m
    if idx2 < len(savecols):
        if savecols[idx2] < B:
            return B - A
        else:
            minval = min(minval, (savecols[idx2] << 1) - A - B)
    if idx1 >= 0:
        minval = min(minval, A + B - (savecols[idx1] << 1))
    return minval


(l, r) = (0, 0)
found_valid = False
last_valid = None
for row in range(0, n):
    if found_valid == False:
        if tr_min[row] != None:
            found_valid = True
            last_valid = row
            l = tr_max[row] - tr_min[row]
            r = tr_max[row] - tr_min[row]
            continue
        continue
    if tr_min[row] == None:
        l += 1
        r += 1
        continue
    ll = find_short_descent(tr_min[last_valid], tr_min[row])
    lr = find_short_descent(tr_min[last_valid], tr_max[row])
    rl = find_short_descent(tr_max[last_valid], tr_min[row])
    rr = find_short_descent(tr_max[last_valid], tr_max[row])
    new_l = min(l + lr, r + rr) + 1 + (tr_max[row] - tr_min[row])
    new_r = min(l + ll, r + rl) + 1 + (tr_max[row] - tr_min[row])
    (l, r) = (new_l, new_r)
    last_valid = row
answ = l + tr_min[last_valid]
print(answ)
