t = int(input())
for i in range(t):
    n = int(input())
    min_r = 10 ** 10
    max_l = -(10 ** 10)
    for j in range(n):
        a, b = list(map(int, input().split()))
        if a > max_l:
            max_l = a
        if b < min_r:
            min_r = b
    print(max(0, -min_r + max_l))
