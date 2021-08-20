t = int(input())
for _ in range(t):
    (n, q) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    best_p = best_m = 0
    for x in a:
        best_p = max(best_p, best_m - x)
        best_m = max(best_m, best_p + x)
    print(max(best_p, best_m))
