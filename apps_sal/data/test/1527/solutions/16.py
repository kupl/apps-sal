from collections import deque
(h, w) = list(map(int, input().split()))
s = [list(input()) for _ in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            cnt = [[-1] * w for _ in range(h)]
            cnt[i][j] = 0
            queue = deque()
            queue.append([i, j])
            for k in range(100 * h * w):
                if len(queue) == 0:
                    break
                num = queue.popleft()
                num1 = num[0]
                num2 = num[1]
                if num1 != 0:
                    if s[num1 - 1][num2] == '.' and cnt[num1 - 1][num2] == -1:
                        cnt[num1 - 1][num2] = cnt[num1][num2] + 1
                        queue.append([num1 - 1, num2])
                if num2 != 0:
                    if s[num1][num2 - 1] == '.' and cnt[num1][num2 - 1] == -1:
                        cnt[num1][num2 - 1] = cnt[num1][num2] + 1
                        queue.append([num1, num2 - 1])
                if num1 != h - 1:
                    if s[num1 + 1][num2] == '.' and cnt[num1 + 1][num2] == -1:
                        cnt[num1 + 1][num2] = cnt[num1][num2] + 1
                        queue.append([num1 + 1, num2])
                if num2 != w - 1:
                    if s[num1][num2 + 1] == '.' and cnt[num1][num2 + 1] == -1:
                        cnt[num1][num2 + 1] = cnt[num1][num2] + 1
                        queue.append([num1, num2 + 1])
            cnt2 = 0
            for k in range(h):
                cnt2 = max(cnt2, max(cnt[k]))
            ans = max(ans, cnt2)
print(ans)
