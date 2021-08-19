import numpy as np
(n, d) = map(int, input().split())
xlist = [list(map(int, input().split())) for i in range(n)]
xarray = np.array(xlist)
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if np.linalg.norm(xarray[i] - xarray[j]) == int(np.linalg.norm(xarray[i] - xarray[j])):
            ans += 1
print(ans)
