import sys
import math


n, k, m = list(map(int, sys.stdin.readline().strip().split(' ')))
word_indexes = {word: i for i, word in enumerate(sys.stdin.readline().strip().split(' '))}
costs = list(map(int, sys.stdin.readline().strip().split(' ')))
min_costs = costs[:]
for ki in range(k):
    group = list(map(int, sys.stdin.readline().strip().split(' ')))
    min_so_far = float('inf')
    for i in group[1:]:
        min_so_far = min(min_so_far, costs[i - 1])
    for i in group[1:]:
        min_costs[i - 1] = min_so_far
sentence = sys.stdin.readline().strip().split(' ')

res = 0
for word in sentence:
    word_index = word_indexes[word]
    res += min_costs[word_index]
print(res)
