import math
X = int(input())


def check_p(X, b):
    p = 0
    while b ** (p + 1) <= X:
        p += 1
    return b ** p


ans = 1
for b in range(2, int(math.sqrt(X)) + 1):
    ans = max(ans, check_p(X, b))
print(ans)
