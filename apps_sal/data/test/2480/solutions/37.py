
from itertools import accumulate
from collections import defaultdict, deque


def resolve():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A = accumulate([a % K for a in A])
    A = [0] + list(A)

    cnt = defaultdict(int)
    q = deque()
    ans = 0
    for r in range(N + 1):
        t = (A[r] - r) % K
        ans += cnt[t]
        cnt[t] += 1

        q.append(t)
        if len(q) == K:
            left = q.popleft()
            cnt[left] -= 1

    print(ans)


def __starting_point():
    resolve()


__starting_point()
