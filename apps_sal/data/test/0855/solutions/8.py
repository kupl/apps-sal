from functools import reduce

def get_scores(a, b):
    if a == b:
        return (0, 0)
    elif (a, b) in ((2, 1), (1, 0), (0, 2)):
        return (1, 0)
    else:
        return (0, 1)

def add(t1, t2):
    return tuple(map(sum, list(zip(t1, t2))))

def mul(t, x):
    return t[0] * x, t[1] * x

k, a, b = list(map(int, input().split(' ')))

alice_ts = {}
bob_ts = {}

for ts in (alice_ts, bob_ts):
    for i in range(3):
        xs = list(map(int, input().split(' ')))[::-1]

        for j in range(3):
            ts[(i, j)] = xs.pop() - 1

state = (a - 1, b - 1)

result = (0, 0)

log = {}
step_results = []

start, end = None, None

for i in range(k):
    if state in log:
        start = log[state]
        end = i

        break

    current_res = get_scores(*state)

    result = add(result, current_res)

    log[state] = i
    step_results.append(current_res)

    if end is not None:
        break

    state = alice_ts[state], bob_ts[state]

if end is not None:
    cycle_sum = reduce(add, step_results[start:end])

    total_cycle_sum = mul(cycle_sum, (k - end) // (end - start))

    result = add(result, total_cycle_sum)

    for i in range(0, (k - end) % (end - start)):
        result = add(result, step_results[start + i])

print(result[0], result[1])

