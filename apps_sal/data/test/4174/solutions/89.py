from itertools import accumulate
(n, x) = map(int, input().split())
L = [0] + list(map(int, input().split()))
acc = list(accumulate(L))
print(sum([1 for i in acc if i <= x]))
