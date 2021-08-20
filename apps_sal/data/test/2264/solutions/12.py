for _ in range(int(input())):
    n = int(input())
    data = []
    max_l = -1
    min_r = 10 ** 10
    for i in range(n):
        (l, r) = list(map(int, input().split()))
        max_l = max(max_l, l)
        min_r = min(min_r, r)
    print(max(max_l - min_r, 0))
