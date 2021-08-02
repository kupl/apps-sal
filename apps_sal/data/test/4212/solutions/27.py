from itertools import combinations_with_replacement as comb
N, M, Q = list(map(int, input().split()))
l = comb(range(1, M + 1), N)
q = [list(map(int, input().split())) for i in range(Q)]
ans = 0
for i in l:
    tmp = 0
    for a, b, c, d in q:
        if i[b - 1] - i[a - 1] == c:
            tmp += d
    ans = max(tmp, ans)
print(ans)
