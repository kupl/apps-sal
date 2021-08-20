from itertools import permutations
N = int(input())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
perm = permutations(range(1, N + 1), N)
cnt = 1
count_a = 0
count_b = 0
for p in perm:
    if p == A:
        count_a = cnt
    if p == B:
        count_b = cnt
    cnt += 1
print(abs(count_a - count_b))
