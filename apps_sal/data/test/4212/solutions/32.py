import itertools
n, m, q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(q)]
maxpt = 0
for lis in itertools.combinations_with_replacement(range(1, m + 1), n):
    forpt = 0
    for i in range(q):
        if lis[abcd[i][1] - 1] - lis[abcd[i][0] - 1] == abcd[i][2]:
            forpt += abcd[i][3]
    maxpt = max(maxpt, forpt)
print(maxpt)
