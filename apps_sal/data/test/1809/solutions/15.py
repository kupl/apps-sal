n, m = [int(x) for x in input().split()]
w = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
ans = 0
state = [0] * n
used = [0] * n
ptr = 0
for i in b:
	if not used[i - 1]:
		used[i - 1] = 1
		state[ptr] = (i, w[i - 1])
		ptr += 1
for i in b:
	ind = state.index((i, w[i - 1]))
	ans += sum(x[1] for x in state[: ind])
	state = [state[ind]] + state[: ind] + state[ind + 1: ]
print(ans)

