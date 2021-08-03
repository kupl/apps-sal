def solve(xs, k, m):
    modded = [[] for _ in range(m)]
    for x in xs:
        modded[x % m].append(x)

    for arr in modded:
        if len(arr) >= k:
            return arr[:k]

    return None


n, k, m = list(map(int, input().split()))
xs = list(map(int, input().split()))[:n]

solution = solve(xs, k, m)
if solution:
    print("Yes")
    print(" ".join(map(str, solution)))
else:
    print("No")
