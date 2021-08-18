import math
import sys
sys.setrecursionlimit(10**6)
q = int(input())


def is_prime(n):
    if n <= 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


a = []
b = []
c = []
for i in range(0, 10**5 + 5):
    a_tmp = is_prime(i)

    if i % 2 == 0:
        b_tmp = False
    else:
        b_tmp = is_prime((i + 1) // 2)

    a.append(a_tmp)
    b.append(b_tmp)
    c.append(a_tmp * b_tmp)

c_sum = [0]
for i in range(1, len(c)):
    c_sum.append(c[i] + c_sum[-1])


for i in range(q):
    l, r = list(map(int, input().split()))
    print((c_sum[r] - c_sum[l - 1]))
