from random import random
from collections import defaultdict
import math
import re
import fractions
N = int(input())
A = list(map(int, input().split(' ')))
arr = [0] * (10 ** 5 + 1)
existing = set()
for a in A:
    arr[a] += 1
    existing.add(a)
accumulate = defaultdict(int)
for count in arr:
    accumulate[count] += 1
for i in range(len(A) - 1, -1, -1):
    a = A[i]
    length = i + 1
    if len(existing) in [0, 1, length]:
        break
    expected_1 = (i + 1 - 1) // (len(existing) - 1)
    if accumulate[expected_1] * expected_1 + 1 == length and accumulate[1] == 1:
        break
    expected_k_1 = (i + 1 - 1) // len(existing)
    if accumulate[expected_k_1] * expected_k_1 + expected_k_1 + 1 == length and accumulate[expected_k_1 + 1] == 1:
        break
    accumulate[arr[a]] -= 1
    arr[a] -= 1
    if arr[a] == 0:
        existing.discard(a)
    accumulate[arr[a]] += 1
print(length)
