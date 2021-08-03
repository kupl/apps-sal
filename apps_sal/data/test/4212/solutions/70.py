import itertools
n, m, q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(q)]
l = list(itertools.combinations_with_replacement(range(1, m + 1), n))
ans = 0
for i in l:
    w = 0
    for j in abcd:
        if i[j[1] - 1] - i[j[0] - 1] == j[2]:
            w += j[3]
    ans = max(ans, w)
print(ans)
