n = int(input())
A = list(map(int, input().split()))

import numpy as np
B = [0 for _ in range(n)]
ans = []
for i, a in enumerate(A[::-1]):
  i = len(A) - i - 1
  B[i] = int(np.array(B[i::i+1]).sum() % 2 != a)
  if B[i] == 1:
    ans.append(i+1)
print(len(ans))
if len(ans) > 0:
  print(*ans)
