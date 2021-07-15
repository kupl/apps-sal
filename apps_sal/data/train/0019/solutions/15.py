from collections import deque

for _ in range(int(input())):
    n, k, d = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ans = len(set(a[:d]))
    now = dict()
    for i in range(d):
        if a[i] in now:
            now[a[i]] += 1
        else:
            now[a[i]] = 1
    for i in range(d, n):
        ans = min(ans, len(now))
        now[a[i - d]] -= 1
        if now[a[i - d]] == 0:
            now.pop(a[i - d])
        if a[i] in now:
            now[a[i]] += 1
        else:
            now[a[i]] = 1
    ans = min(ans, len(now))
    print(ans)

