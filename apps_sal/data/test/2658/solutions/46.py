from collections import deque


def solve(A, K):
    a = deque()
    seen = [False for _ in range(len(A))]
    cur = 0
    while True:
        if seen[cur]:
            while a[0] != cur:
                K -= 1
                a.popleft()
                if K == 0:
                    return a[0] + 1
            break
        a.append(cur)
        seen[cur] = True
        cur = A[cur]
    return a[K % len(a)] + 1


(N, K) = map(int, input().split())
A = list(map(int, input().split()))
A = [v - 1 for v in A]
print(solve(A, K))
