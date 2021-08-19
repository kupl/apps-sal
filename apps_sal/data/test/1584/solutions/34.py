import bisect


def binary_search(items, a, b, i, j):
    def c_is_x(c):
        is1 = c > max(a - b, b - a)
        is2 = c < a + b

        if is1 and is2:
            return 0
        elif is1:
            return 1
        else:
            return 2

    low = j + 1
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2
        ans = items[mid]
        c_type = c_is_x(ans)
        if c_type == 0 and mid != i and mid != j:
            return mid
        elif c_type == 1:
            low = mid + 1
        else:
            high = mid - 1

    return None


N = int(input())
L = list(map(int, input().split()))

L.sort()
# print(L)
count = 0
for i in range(N):
    for j in range(i + 1, N):
        # i = N - i - 1
        # j = N - j - 1
        a = L[i]
        b = L[j]
        k = bisect.bisect_left(L, a + b, lo=j) - 1

        if k < N:
            c = L[k]
            # print(a, b, c, a+b)
            # print(i, j, k)
            count += max(k - j, 0)


print(count)
