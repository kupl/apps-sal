(citys, cap) = map(int, input().split())
if citys - 1 <= cap:
    print(citys - 1)
else:
    n = citys - cap
    print(n * (n + 1) // 2 + cap - 1)
