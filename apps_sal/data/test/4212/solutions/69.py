import itertools
(N, M, Q) = list(map(int, input().split()))
ABCD = [[int(x) for x in input().split()] for i in range(Q)]
ans = 0
for A in itertools.combinations_with_replacement([m for m in range(1, M + 1)], N):
    ans2 = 0
    for (a, b, c, d) in ABCD:
        if A[b - 1] - A[a - 1] == c:
            ans2 += d
    ans = max(ans, ans2)
print(ans)
