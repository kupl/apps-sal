def bin_search(k):
    l = -1
    r = n - 1
    while r - l > 1:
        h = (l + r) // 2
        if lst1[h] > k:
            r = h
        else:
            l = h
    if lst1[r] <= k:
        return r + 1
    else:
        return r


(n, m) = [int(x) for x in input().split()]
lst1 = [int(x) for x in input().split()]
lst2 = [int(x) for x in input().split()]
lst1.sort()
for i in range(m):
    print(bin_search(lst2[i]), end=' ')
