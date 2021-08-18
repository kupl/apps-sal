
N = int(input())

list_plus = []
list_minus = []
for i in range(N):
    S = input()
    state = 0
    min_state = 0
    for s in S:
        if s == '(':
            state += 1
        else:
            state -= 1
        min_state = min(min_state, state)

    if state > 0:
        list_plus.append((min_state, state))
    else:
        list_minus.append((min_state - state, -state))


def compute(arr):
    total_state = 0
    for min_state, state in arr[::-1]:
        if total_state + min_state < 0:
            print('No')
            return
        total_state += state
    return total_state


list_plus.sort()
total_state_plus = compute(list_plus)
list_minus.sort()
total_state_minus = compute(list_minus)

print('Yes' if total_state_plus == total_state_minus else 'No')
