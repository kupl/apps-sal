x, k, d = list(map(int, input().split()))
if abs(x) // d >= k:
    # print("ひ")
    print((abs(x) - d * k))
elif (k - abs(x) // d) % 2 == 0:
    # print("fu")
    print((abs(x) % d))
else:
    # print("mi")
    print((d - abs(x) % d))
