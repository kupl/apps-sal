import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
(N, K) = map(int, input().split())
V = list(map(int, input().split()))
ans = 0
for pick in range(min(K + 1, N + 1)):
    for right in range(pick + 1):
        left = pick - right
        pick_list = V[:right] + V[N - left:]
        pick_list = sorted(pick_list)
        tmp_ans = sum(pick_list)
        rem = min(K - pick, len(pick_list))
        for i in range(rem):
            if pick_list[i] < 0:
                tmp_ans -= pick_list[i]
            else:
                break
        ans = max(tmp_ans, ans)
print(ans)
