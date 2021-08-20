N = int(input())
S = input()


def f(m):
    se = set()
    arr = [None] * N
    for i in range(0, N - m + 1):
        if i >= m:
            se.add(arr[i - m])
        arr[i] = hash(S[i:i + m])
        if arr[i] in se:
            return True
    return False


l = 0
r = N // 2 + 1
while r - l > 1:
    mid = (r + l) // 2
    if f(mid):
        l = mid
    else:
        r = mid
print(l)
