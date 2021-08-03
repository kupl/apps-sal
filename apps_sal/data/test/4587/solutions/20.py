def bs_left(list, target):
    low = 0
    high = len(list)

    while low < high:
        mid = (low + high) // 2
        if target > list[mid]:
            low = mid + 1
        else:
            high = mid
    return low


def bs_right(list, target):
    low = 0
    high = len(list)
    while low < high:
        mid = (low + high) // 2
        if target < list[mid]:
            high = mid
        else:
            low = mid + 1
    return low


n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
C.sort()

ans = 0
for b in B:
    ans += (bs_left(A, b) * (n - bs_right(C, b)))
print(ans)
