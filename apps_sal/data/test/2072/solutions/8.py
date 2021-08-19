N = int(input())
X = list(map(int, input().split()))
V = list(map(int, input().split()))


def calc(p):
    return max((abs(X[i] - p) / V[i] for i in range(N)))


(lb, ub) = (1.0, 1000000000.0)
while ub - lb > 5e-07:
    mid = (lb + ub) / 2
    if calc(mid - 4e-07) < calc(mid + 4e-07):
        ub = mid
    else:
        lb = mid
print('%.9f' % calc(lb))
