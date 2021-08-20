t = int(input())
for i in range(t):
    (n, p, k) = list(map(int, input().split()))
    goods = list(map(int, input().split()))
    goods.sort()
    if goods[0] > p:
        print(0)
        continue
    elif len(goods) == 1:
        print(1)
        continue
    hi = n
    lo = 0
    odd_index_sums = [goods[1]]
    even_index_sums = [goods[0]]
    for i in range(2, n):
        if i % 2 == 0:
            even_index_sums.append(even_index_sums[-1] + goods[i])
        else:
            odd_index_sums.append(odd_index_sums[-1] + goods[i])
    while lo < hi - 1:
        mid = lo + (hi - lo) // 2
        if mid % 2 == 0:
            cost = even_index_sums[mid // 2]
        else:
            cost = odd_index_sums[mid // 2]
        if cost <= p:
            lo = mid
        else:
            hi = mid
    print(hi)
