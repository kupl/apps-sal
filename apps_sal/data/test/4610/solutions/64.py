import collections
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

a_cnt = collections.Counter(a)
a_sort = sorted(list(a_cnt.values()), reverse=True)
print((sum(a_sort[k:])))
