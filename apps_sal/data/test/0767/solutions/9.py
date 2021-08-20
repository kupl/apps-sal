(n, z) = list(map(int, input().split()))
arrs = [int(x) for x in input().split()]
arrs.sort()


def fi():
    j = len(arrs) // 2
    while arrs[j] - arrs[0] < z and j < len(arrs) - 1:
        j += 1
    l = 0
    r = j
    arr = arrs[:]
    cnt = 0
    while r != len(arr):
        if arr[l] == 10 ** 10:
            l += 1
        elif arr[r] - arr[l] >= z:
            arr[r] = 10 ** 10
            cnt += 1
            r += 1
            l += 1
        else:
            r += 1
    return cnt


print(fi())
