n = int(input())
l = list(map(int, input().split()))
c1 = l.count(1)
c2 = l.count(2)
if c1 == 0 or c2 == 0:
    ll = l
else:
    ll = [2, 1]
    l1 = [1] * (c1 - 1)
    l2 = [2] * (c2 - 1)
    ll = ll + l2 + l1
print(' '.join(map(str, ll)))
