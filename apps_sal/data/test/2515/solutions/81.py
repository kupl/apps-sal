import itertools
Q = int(input())
l = [0 for q in range(Q)]
r = [0 for q in range(Q)]
for q in range(Q):
    (l[q], r[q]) = map(int, input().split(' '))
max_r = max(r)
prime_numbers = [True for n in range(max_r + 1)]
similar_numbers = [False for n in range(max_r + 1)]
(prime_numbers[0], prime_numbers[1]) = (False, False)
for divisor in range(2, max_r // 2 + 1):
    if prime_numbers[divisor]:
        for multipler in range(2, max_r // divisor + 1):
            prime_numbers[divisor * multipler] = False
for N in range(1, max_r + 1, 2):
    if prime_numbers[N] and prime_numbers[(N + 1) // 2]:
        similar_numbers[N] = True
accumulate_sim_nums = list(itertools.accumulate(map(int, similar_numbers)))
for q in range(Q):
    print(accumulate_sim_nums[r[q]] - accumulate_sim_nums[l[q] - 1])
