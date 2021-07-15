from collections import Counter
input()
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
print(next(iter((Counter(a) - Counter(b)).keys())))
print(next(iter((Counter(b) - Counter(c)).keys())))
