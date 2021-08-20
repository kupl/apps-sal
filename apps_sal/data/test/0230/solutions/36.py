from collections import deque
N = int(input())
S = input()


def f(m):
    se = set()
    q = deque()
    for i in range(0, N - m + 1):
        h = hash(S[i:i + m])
        q.append(h)
        if h in se:
            return True
        if len(q) >= m:
            se.add(q.popleft())
    return False


l = 0
r = N // 2 + 1
while r - l > 1:
    mid = (r + l) // 2
    if f(mid):
        l = mid
    else:
        r = mid
print(l)
