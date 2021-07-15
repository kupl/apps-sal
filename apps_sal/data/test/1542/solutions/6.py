def b_s(a, key):
    left = -1
    right = len(a)

    while right - left > 1:
        m = (left + right) // 2
        if a[m] > key:
            right = m
        else:
            left = m
    return right

n = int(input())
cost = sorted(list(map(int, input().split())))
q = int(input())

for i in range(q):
    m = int(input())
    x = b_s(cost, m)
    print(x)
