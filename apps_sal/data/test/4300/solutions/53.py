import itertools as itr
n = input()
d = map(int, input().split())
k = itr.combinations(d, 2)
sum_k = sum([a * b for (a, b) in k])
print(sum_k)
