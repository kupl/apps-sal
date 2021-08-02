L = list(map(int, input().split()))
tmp = 3 * max(L) - sum(L)
if tmp % 2 == 0:
    print((tmp // 2))
else:
    print(((tmp + 3) // 2))
