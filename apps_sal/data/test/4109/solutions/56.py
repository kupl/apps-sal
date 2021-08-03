import numpy as np
n, m, x = map(int, input().split())
costs = []
understnding = []
ans = 10 ** 20

for _ in range(n):
    tmp = list(map(int, input().split()))
    costs.append(tmp[0])
    understnding.append(tmp[1:])

costs = np.array(costs)
understnding = np.array(understnding)

for i in range(1, 2**n):
    row = str(bin(i)).split("0b")[1]
    row = '0' * (n - len(row)) + row
    one_index = [j for j in range(len(row)) if row[j] == "1"]
    cost_sum = np.sum(costs[one_index])
    under_sum = np.sum(understnding[one_index], axis=0)
    if np.all(under_sum >= x) and cost_sum < ans:
        ans = cost_sum

if ans == 10 ** 20:
    print(-1)
else:
    print(ans)
