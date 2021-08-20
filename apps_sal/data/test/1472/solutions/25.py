from collections import deque
(N, X, Y) = map(int, input().split())
ans_list = [0 for _ in range(N - 1)]
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        ans1 = j - i
        ans2 = abs(i - X) + 1 + abs(j - Y)
        ans_list[min(ans1, ans2) - 1] += 1
print(*ans_list, sep='\n')
