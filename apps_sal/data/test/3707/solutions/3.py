n, t, k, d = list(map(int, input().split()))
clk = 0
s = 0
while s < n:
    s += k
    clk += t
clk2 = 0
lb, ub = 0, int(1e10)
while lb <= ub:
    mid = lb + ub >> 1
    s = mid // t * k + max(0, mid - d) // t * k
    if s >= n:
        clk2 = mid
        ub = mid - 1
    else:
        lb = mid + 1

print(["NO", "YES"][clk > clk2])
