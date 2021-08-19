n, m = list(map(int, input().split()))
res = 0
if n > m // 2:
    res = m // 2
    print(res)
else:
    res = n
    n -= res
    m -= res * 2
    # ここでnは0
    res += m // 4
    print(res)
