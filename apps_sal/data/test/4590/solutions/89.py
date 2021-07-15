import numpy as np
n, m, k = map(int, input().split())
li_a = np.array(list(map(int, input().split())))
li_b = np.array(list(map(int, input().split())))
a_i, b_i = np.hstack([np.array([0]),li_a.cumsum()]), np.hstack([np.array([0]),li_b.cumsum()])

j = m
ans = 0
for i in range(n+1):
    if a_i[i]>k:
        break
    while(b_i[j] > k - a_i[i]):
        j -= 1
    ans = max(ans, i+j)
print(ans)
