import itertools
import math

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
p_no, q_no = 0, 0

per = [c + 1 for c in range(n)]
per_list = list(itertools.permutations(per))

for i in range(math.factorial(n)):
    if p == per_list[i]:
        p_no = i
    if q == per_list[i]:
        q_no = i

print(abs(p_no - q_no))
