SIZE = 171000
L = [i ** 3 for i in range(SIZE)]

def get_count(n):
    MAX = int(n ** (1 / 3)) + 1
    if L[MAX] > n:
        MAX -= 1

    res = 0
    for i in range(2, MAX + 1):
        x = n // L[i]
        if x != 1:
            res += x
        else:
            res += MAX - i + 1
            break
    return res

def bin_search(m):
    beg = int(4.8 * m)
    end = min(8 * m, int(5e15))
    while beg <= end:
        mid = (beg + end) // 2
        count_mid = get_count(mid)
        if count_mid == m:
            if beg == end:
                return mid
            end = mid
        elif count_mid > m:
            end = mid - 1
        else:
            beg = mid + 1
    return -1

m = int(input())
print(bin_search(m))

