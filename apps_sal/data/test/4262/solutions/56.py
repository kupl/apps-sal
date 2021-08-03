import math
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))


def dic_order(a):
    b = [x for x in range(1, n + 1)]
    cnt = 1
    for i in range(n - 1):
        cnt += b.index(a[i]) * math.factorial(n - i - 1)
        b.remove(a[i])
    return cnt


p_order = dic_order(p)
q_order = dic_order(q)
print(abs(p_order - q_order))
