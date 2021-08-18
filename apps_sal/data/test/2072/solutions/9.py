N = int(input())

X = list(map(int, input().split()))
V = list(map(int, input().split()))


def calc(p):
    return max(abs(X[i] - p) / V[i] for i in range(N))


lb, ub = 1.0, 1e9
while ub - lb > 5e-7:
    mid = (lb + ub) / 2
    if calc(mid - 5e-7) < calc(mid + 5e-7):
        ub = mid
    else:
        lb = mid

print("%.9f" % calc(lb))
