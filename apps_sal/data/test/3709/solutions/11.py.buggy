import sys
N, K = list(map(int, input().split()))

states = set([(0, 0)])

for _ in range(N):
    can_solve = list(map(int, input().split()))

    next_states = set()
    for (selected, bm) in states:
        cnts = [(bm >> i) & 1 for i in range(K)][::-1]

        next_cnts = [cnts[i] + can_solve[i] for i in range(K)]
        next_selected = selected + 1

        if max(next_cnts) <= next_selected / 2 and next_selected > 0:
            print("YES")

            return

        if max(next_cnts) <= 1 and next_selected <= 4:
            bin_num = int(''.join(map(str, next_cnts)), 2)
            next_states.add((next_selected, bin_num))

    states |= next_states

print("NO")
