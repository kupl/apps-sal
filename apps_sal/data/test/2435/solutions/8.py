T = int(input())
for __ in range(T):
    n, x, m = list(map(int, input().split()))
    i, j = x, x
    for __ in range(m):
        l, r = list(map(int, input().split()))
        if r >= i:
            i = min(i, l)
        if l <= j:
            j = max(j, r)
    print(j - i + 1)

