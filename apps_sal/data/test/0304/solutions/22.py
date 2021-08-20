from itertools import product
from math import factorial
from operator import mul
from functools import reduce
seen = input()
counts = [[0] for digit in range(10)]
for digit in map(int, seen):
    counts[digit].append(counts[digit][-1] + 1)
for digit in range(10):
    if len(counts[digit]) > 1:
        counts[digit].pop(0)
answer = 0
for count in product(*counts):
    answer += factorial(sum(count)) // reduce(mul, (factorial(count[digit]) for digit in range(10)))
    if count[0] > 0:
        count = list(count)
        count[0] -= 1
        answer -= factorial(sum(count)) // reduce(mul, (factorial(count[digit]) for digit in range(10)))
print(answer)
