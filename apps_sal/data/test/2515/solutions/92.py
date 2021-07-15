import numpy as np
q = int(input())
p = np.array([0]*(10**5+1))
for i in range(2, 10**5+1):
    p[::i] += 1
like = [0, 0, 0]
for j in range(3, 10**5+1):
    if p[j] == 1 and p[(j+1)//2] == 1:
        plus = 1
    else:
        plus = 0
    like.append(like[-1]+plus)

for _ in range(q):
    l, r = map(int, input().split())
    ans = like[r]-like[l-1]
    print(ans)
