N = int(input())
P = "".join(input().split())
Q = "".join(input().split())
base = [str(i) for i in range(1, N + 1)]
import itertools as itr
permutations = itr.permutations(base)
patterns = ["".join(value) for value in permutations]
patterns.sort()
p_index = patterns.index(P)
q_index = patterns.index(Q)
print(abs(p_index - q_index))
