
N = int(input())
S = input()


num_E = [0] * N
num_W = [0] * N
max_num = 0
leader_index = 0
for i, c in enumerate(S):
    if c == "W":
        num_W[i] = num_W[i - 1] + 1
        num_E[i] = num_E[i - 1]
    else:
        num_W[i] = num_W[i - 1]
        num_E[i] = num_E[i - 1] + 1
    tmp = num_E[i] - num_W[i]
    if max_num < tmp:
        leader_index = i
        max_num = tmp

print(S[:leader_index].count("W") + S[leader_index + 1:].count("E"))
