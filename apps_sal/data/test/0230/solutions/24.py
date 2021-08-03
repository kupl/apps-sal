from collections import deque

N = int(input())
S = input()


def exists(length):
    que = deque()
    V = set()
    for left in range(N - length + 1):
        if left > length - 1:
            V.add(que.popleft())
        T = S[left: left + length]
        if T in V:
            return True
        que.append(T)
    return False


ok = 0
ng = N
while ng - ok > 1:
    mid = (ok + ng) // 2

    if exists(mid):
        ok = mid
    else:
        ng = mid

print(ok)
