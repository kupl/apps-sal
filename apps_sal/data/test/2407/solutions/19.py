import sys
input = sys.stdin.readline
for _ in range(int(input())):
    (n, r) = map(int, input().split())
    x = sorted(set(map(int, input().split())))
    cnt = 0
    now_right_idx = len(x) - 1
    total_explosion = 0
    while now_right_idx >= 0:
        cnt += 1
        total_explosion += r
        now_right_idx -= 1
        while now_right_idx >= 0 and x[now_right_idx] <= total_explosion:
            now_right_idx -= 1
    print(cnt)
