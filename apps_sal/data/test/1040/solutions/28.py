from collections import deque
n = int(input())
s = deque(list(input()))
ans = deque()
while s:
    ans.append(s.popleft())
    if len(ans) >= 3:
        if ans[-3] == 'f' and ans[-2] == 'o' and (ans[-1] == 'x'):
            for _ in range(3):
                ans.pop()
print(len(ans))
