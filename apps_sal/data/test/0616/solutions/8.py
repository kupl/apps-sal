N, M = list(map(int, input().split()))
A = []
min_state = [10**9] * (2**N)
min_state[0] = 0
for _ in range(M):
    a, b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    key = 0
    for tmp in c:
        key += 2**(tmp - 1)
    A.append((a, key))
L = len(min_state)
for a, key in A:
    for i, score in enumerate(min_state):
        next_key = key | i

        if min_state[next_key] > score + a:
            min_state[next_key] = score + a
if min_state[-1] == 10**9:
    print((-1))
else:
    print((min_state[-1]))
