import sys
import numpy as np
n = int(input())
a = [int(input()) for _ in range(n)]
mx = str(max(a))
mx_id = a.index(int(mx))
a.remove(int(mx))
mx_sub = str(max(a))
ans = '\n'.join((mx if i != mx_id else mx_sub for i in range(n)))
print(ans)
