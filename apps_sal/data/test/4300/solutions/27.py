from itertools import permutations
n = int(input())
d = [int(i) for i in input().split()]
t = sum([i[0] * i[1] for i in permutations(d, 2)]) // 2
print(t)
