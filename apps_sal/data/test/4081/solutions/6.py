from collections import *

n = int(input())

M = deque(list(map(int, input().split())))

ans = []
last = None
while len(M) > 0:
    if ans == []:
        if M[-1] <= M[0]:
            ans += ['R']
            last = M[-1]
            M.pop()
        else:
            ans += ['L']
            last = M[0]
            M.popleft()
    else:
        if M[-1] <= last and M[0] <= last:
            break

        if M[-1] <= last:
            ans += ["L"]
            last = M[0]
            M.popleft()
            continue

        if M[0] <= last:
            ans += ['R']
            last = M[-1]
            M.pop()
            continue

        if M[0] <= M[-1]:
            ans += ["L"]
            last = M[0]
            M.popleft()
        elif M[-1] <= M[0]:
            ans += ["R"]
            last = M[-1]
            M.pop()

print(len(ans))
print("".join(ans))
