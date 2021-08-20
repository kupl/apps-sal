(N, K) = list(map(int, input().split()))
A = list(map(int, input().split()))


def check(l):
    count = 0
    for L in A:
        count += L // l
        if L % l != 0:
            count += 1
        count -= 1
    return count <= K


(bottom, top) = (0, max(A))
while top - bottom > 1:
    mid = (top + bottom) // 2
    if check(mid):
        top = mid
    else:
        bottom = mid
print(top)
