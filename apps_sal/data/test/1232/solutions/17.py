(n, m) = map(int, input().split())
(k, l) = map(int, input().split())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
if lst1[k - 1] < lst2[m - l]:
    print('YES')
else:
    print('NO')
