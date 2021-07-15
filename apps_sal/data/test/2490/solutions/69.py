s = input()
state = [0, 1]
for i in s:
    n = int(i)
    state_new = [min(state[0] + n, state[1] + 10 - n), 
                 min(state[0] + n + 1, state[1] + 9 - n)]
    state = state_new
print(state[0])
