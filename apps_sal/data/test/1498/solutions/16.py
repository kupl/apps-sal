import sys
input = sys.stdin.readline
(n, q) = map(int, input().split())
T = [0] * n
for _ in range(q):
    (t, k, d) = map(int, input().split())
    new_T = T[:]
    cnt = 0
    ans = 0
    for i in range(n):
        if new_T[i] < t:
            new_T[i] = t + d - 1
            cnt += 1
            ans += i + 1
        if cnt == k:
            break
    if cnt == k:
        T = new_T
        print(ans)
    else:
        print(-1)
