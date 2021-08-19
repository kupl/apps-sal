def solve():
    (k, a, b) = list(map(int, input().strip().split()))
    ak = a // k
    bk = b // k
    if a % k != 0 and bk == 0:
        return -1
    if b % k != 0 and ak == 0:
        return -1
    return ak + bk


print(solve())
