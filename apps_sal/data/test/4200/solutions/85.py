# coding: utf-8
# Your code here!

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

a.sort(reverse=True)
total = sum(a)
if all([x >= total / (4 * m) for x in a[:m]]):
    print('Yes')
else:
    print('No')
