import numpy as np
N = int(input())
X_ls = np.array(list(map(int, input().split())))


ans = 0
for p in range(max(X_ls) + 1):
    sub = X_ls - p
    ans_1 = sum(sub**2)
    if ans_1 <= ans or ans == 0:
        ans = ans_1
print(ans)
