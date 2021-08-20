(n, x, y) = list(map(int, input().split()))
ans_ls = [0] * (n - 1)
for start in range(1, n):
    for end in range(start + 1, n + 1):
        cost_1 = end - start
        cost_2 = abs(start - x) + abs(end - y) + 1
        cost = min(cost_1, cost_2)
        ans_ls[cost - 1] += 1
for ans in ans_ls:
    print(ans)
