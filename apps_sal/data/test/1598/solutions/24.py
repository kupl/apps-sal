data = [int(i) for i in input()]
n = len(data)
minval = [0] * n
minval[-1] = 2 * data[-1] - 1

for i in range(n - 2, -1, -1):
    if data[i] == 1:
        minval[i] = min(1, minval[i + 1] + 1)
    else:
        minval[i] = min(-1, minval[i + 1] - 1)

ans = [i for i in data]
for i in range(n - 1, -1, -1):
    if minval[i] == 1:
        ans[i] = 0
ans2 = [str(i) for i in ans]

print("".join(ans2))
# print(minval)
