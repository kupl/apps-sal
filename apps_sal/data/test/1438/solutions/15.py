(n, k) = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def Possible(x):
    powder = k
    for i in range(n):
        cnt = B[i] // A[i]
        if cnt < x:
            powder -= A[i] * x - B[i]
            if powder < 0:
                return False
    return True


left = 0
right = 10 ** 9 + 10 ** 9 + 10
while left + 1 < right:
    mid = (left + right) // 2
    if Possible(mid):
        left = mid
    else:
        right = mid
print(left)
