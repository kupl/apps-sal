(h, n) = map(int, input().split())
lst = list(map(int, input().split()))
if sum(lst) < h:
    print('No')
else:
    print('Yes')
