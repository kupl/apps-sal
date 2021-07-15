from itertools import accumulate

MAX_T = 10 ** 5 + 100
MAX_C = 30

n, c = list(map(int, input().split()))
time = {c: [] for c in range(1, MAX_C + 1)}

for _ in range(n):
    s, t, c = list(map(int, input().split()))
    time[c].append((s, t))

n_program = [0 for _ in range(MAX_T + 1)]

for c in range(1, MAX_C + 1):

    recording = [0 for _ in range(MAX_T + 1)]

    for s, t in time[c]:
        recording[s] += 1
        recording[t + 1] -= 1

    recording = accumulate(recording)

    for i, r in enumerate(recording):
        if r:
            n_program[i] += 1

answer = max(n_program)
print(answer)

