
N, M = list(map(int, input().rstrip().split()))
ans = []
delta = 0
visited = set()


for i in range(M):
    L = 1 + i
    R = N - i
    diff = (R - delta) - L

    if (2 * diff == N) or \
       (diff in visited) or ((N - diff) in visited):

        delta = 1

    ans.append([L, R - delta])
    visited |= {diff, (N - diff)}


for nums in ans:
    print((*nums))
