import itertools
import math
N = int(input())
A = []
b = []
count = 0
nums = [i for i in range(N)]
for balls in itertools.permutations(nums):
    b.append(list(balls))

for i in range(N):
    A.append(list(map(int, input().split())))
for j in range(N - 1):
    for i in b:
        count += math.sqrt(pow(A[i[j]][0] - A[i[j + 1]][0], 2) + pow(A[i[j]][1] - A[i[j + 1]][1], 2))

print(count / math.factorial(N))
