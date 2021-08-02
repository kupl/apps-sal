import numpy as np

abc = np.array([int(a) for a in input().split()])
abc = abc - np.array([np.min(abc)] * 3)
abc = np.sort(abc)
ans = 0
if abc[1] == 0:
    ans = abc[2]
elif abc[1] % 2 == 0:
    ans += abc[1] // 2
    ans += abc[2] - abc[1]
else:
    ans += 1
    abc[0] += 1
    abc[2] += 1
    ans += (abc[1] - abc[0]) // 2
    ans += abc[2] - abc[1]
print(ans)
