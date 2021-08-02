from collections import deque


def follow(idx, this_or_first_free):
    if idx == -2:
        return -2

    if this_or_first_free[idx] == -1:
        return idx
    if this_or_first_free[idx] == -2:
        return -2

    root = follow(this_or_first_free[idx], this_or_first_free)
    this_or_first_free[idx] = root
    return root


def take(idx, this_or_first_free, initial_next):
    this_or_first_free[idx] = initial_next[idx]  # this can be -2 or an index to follow


def legit(idx):
    return idx != -1 and idx != -2


(n, m, d) = list(map(int, input().split()))
break_list = list([(int(idx_val[1]), idx_val[0]) for idx_val in enumerate(input().split())])

break_list.sort()

assignment = [-1] * n
breaks_initial_next = [-2] * n

TFO = [False] * n

deq = deque()
for i in range(n):
    val = break_list[i][0]  # pos of this break
    deq.append((val, i))  # append the pos and its index in the array

    while len(deq) > 0 and val - deq[0][0] - 1 >= d:
        breaks_initial_next[deq[0][1]] = i
        deq.popleft()

head_initial_next = [i + 1 for i in range(n)]
head_initial_next[-1] = -2
head_first_free = [-1] * n

first_not_taken = 0
days_count = 0
while legit(first_not_taken):
    current = first_not_taken
    days_count += 1

    while legit(current):
        take(current, head_first_free, head_initial_next)  # invalidate head
        assignment[break_list[current][1]] = days_count

        if not TFO[current]:
            TFO[current] = True
            current = breaks_initial_next[current]

        current = follow(current, head_first_free)

    first_not_taken = follow(first_not_taken, head_first_free)  # find next head

print(days_count)
print(str(assignment)[1:-1].replace(",", ""))
