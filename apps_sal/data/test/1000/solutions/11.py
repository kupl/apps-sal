def solve(n, v):
    fuel = min(n - 1, v)
    cost = fuel
    for i in range(2, n):
        if fuel >= n - 1:
            break
        fuel += 1
        cost += i
    return cost

n, v = list(map(int, input().split()))
print(solve(n, v))

