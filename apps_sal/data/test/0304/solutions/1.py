N = input()

C = [0]*10
for n in N:
    C[int(n)] += 1

memo = {}
def dfs(i, state):
    key = tuple(state)
    if key in memo:
        return memo[key]
    r = 0
    if all(s == 0 or 1 <= t for s, t in zip(C, state)):
        r += 1
    for j in range(10):
        if C[j] - state[j] > 0:
            state[j] += 1
            r += dfs(i+1, state)
            state[j] -= 1
    memo[key] = r
    return r
state = [0]*10
ans = 0
for i in range(1, 10):
    if C[i] > 0:
        state[i] += 1
        ans += dfs(1, state)
        state[i] -= 1
print(ans)
