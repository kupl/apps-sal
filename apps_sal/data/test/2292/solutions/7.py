from collections import Counter
T = int(input().strip())
for t in range(T):
    n = int(input().strip())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if Counter(a) != Counter(b):
        print('No')
        continue
    mid = n // 2 + n % 2
    aa = Counter(tuple(sorted([a[i], a[n - i - 1]])) for i in range(mid))
    bb = Counter(tuple(sorted([b[i], b[n - i - 1]])) for i in range(mid))

    # print(aa)
    # print(bb)
    if aa != bb:
        print('No')
        continue
    print('Yes')
