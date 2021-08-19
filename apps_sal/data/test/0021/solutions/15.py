n = int(input())
L = list(map(int, input().split()))
(index1, index2) = (L.index(1), L.index(n))
if index1 > index2:
    (index1, index2) = (index2, index1)
d = index2 - index1
d = max(d, n - 1 - index1)
d = max(d, index2)
print(d)
