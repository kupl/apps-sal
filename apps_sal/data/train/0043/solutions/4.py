def f(aa, bb, target):
    total = 0
    for i in range(len(aa)):
        if aa[i] > target:
            total += bb[i]

    return total <= target


t = int(input())

for case in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    low = 1
    high = 1000000000

    while low < high:
        mid = (low + high) // 2
        res = f(a, b, mid)
        if res:
            # mid is possible
            high = mid
        else:
            low = mid + 1

    print(low)
