import collections
N, K = map(int, input().split())
A = list(map(int, input().split()))


cA = collections.Counter(A)

sorted_ls = sorted(list(cA.values()))
sum_ls = sum(sorted_ls)


if len(sorted_ls) > K:
    print(sum(sorted_ls[:len(sorted_ls) - K]))
else:
    print(0)
