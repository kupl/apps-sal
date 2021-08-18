from math import ceil
n = int(input())
a = list(map(int, input().split()))
cur_state_sasha = 0
cur_state_dima = 0
a = [(p, i) for i, p in enumerate(a)]
a.sort()
ans = 0
for i in range(0, 2 * n, 2):
    ans += abs(a[i][1] - cur_state_sasha)
    cur_state_sasha = a[i][1]
    ans += abs(a[i + 1][1] - cur_state_dima)
    cur_state_dima = a[i + 1][1]

print(ans)
