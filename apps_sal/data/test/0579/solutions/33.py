from collections import deque
def it(): return list(map(int, input().strip().split()))


def maximise(L, R, cycle):
    cur = 0
    ans = max(cycle)
    queue = deque([0])
    dp = [0] * (2 * L + 1)
    for i, num in enumerate(cycle + cycle):
        j = i + 1
        cur += num
        while queue and j - queue[0] > R:
            queue.popleft()
        if queue:
            ans = max(ans, cur - dp[queue[0]])
        while queue and dp[queue[-1]] >= cur:
            queue.pop()
        queue.append(j)
        dp[j] = cur
    return ans


def get(K, cycle):
    L = len(cycle)
    T = sum(cycle)

    if K > L:
        B = (K - 1) // L
        R = K - B * L
    else:
        B = 0
        R = K
    return max(maximise(L, K, cycle), maximise(L, R, cycle) + max(0, B * T))


def solve():
    N, K = it()
    P = it()
    C = it()

    for i in range(N):
        P[i] -= 1

    cycles = []
    seen = [False] * N
    for i in range(N):
        if not seen[i]:
            cycle = []
            first = curr = i
            while True:
                seen[curr] = True
                cycle.append(C[curr])
                curr = P[curr]
                if curr == first:
                    break
            cycles.append(cycle)

    ans = float('-inf')
    for cycle in cycles:
        ans = max(ans, get(K, cycle))
    return ans


def __starting_point():
    ans = solve()
    print(ans)


__starting_point()
