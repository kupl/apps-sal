import sys

def ii():
    return sys.stdin.readline().strip()

def idata():
    return [int(x) for x in ii().split()]

def solve_of_problem():
    n = int(ii())
    data = idata()
    ans = [data[0]]
    for i in range(1, n - 1):
        if data[i - 1] < data[i] > data[i + 1] or data[i - 1] > data[i] < data[i + 1]:
            ans += [data[i]]
    print(len(ans) + 1)
    print(*ans, data[-1])
    return

for ______ in range(int(ii())):
    solve_of_problem()
