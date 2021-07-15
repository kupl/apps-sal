from math import sqrt

n = int(input())

ans = int(sqrt(n))

if (ans + 1) * (ans + 1) <= n:
    print((ans + 1) * (ans + 1))
elif ans * ans <= n:
    print(ans * ans)
else:
    print((ans - 1) * (ans - 1))
