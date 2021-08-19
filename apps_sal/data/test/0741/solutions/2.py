(n, M) = list(map(int, input().split()))
data = list(map(int, input().split()))
state = False
states = [0 for i in range(n + 1)]
states[0] = (data[0], 0)
for i in range(1, n + 1):
    value = (M if i == n else data[i]) - data[i - 1]
    states[i] = (states[i - 1][0] + (value if state else 0), states[i - 1][1] + (0 if state else value))
    state = not state
ans = states[n][0]
for i in range(n + 1):
    if (M if i == n else data[i]) - (data[i - 1] if i > 0 else 0) > 1:
        val = 0
        if i != 0 and i != n:
            val = states[i - 1][0] + states[n][1] - states[i][1]
            val += data[i] - data[i - 1] - 1
        if i == 0:
            val = states[n][1]
            val += data[0] - 1
        if i == n:
            val = states[n - 1][0]
            val += M - data[n - 1] - 1
        ans = max(ans, val)
print(ans)
