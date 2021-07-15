t = int(input())
for _ in range(t):
    n, k = [int(i) for i in input().split()]
    x = [int(i)-1 for i in input().split()]
    boundary_maxdiff = max(x[0], n-1-x[-1])
    maxdiff = max(x[i+1]-x[i] for i in range(len(x)-1)) if len(x) >= 2 else 0  # 0-0 1-0 2-1 3-1 4-2 5-2
    maxdiff = maxdiff // 2
    print(max(maxdiff, boundary_maxdiff) + 1)
