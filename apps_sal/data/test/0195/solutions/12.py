import time
(A, B, C, N) = (int(i) for i in input().split())
start = time.time()
ans = N + C - A - B
if ans <= 0 or C > A or C > B:
    ans = -1
print(ans)
finish = time.time()
