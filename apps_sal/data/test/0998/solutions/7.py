n, x = list(map(int, input().split()))
nn = 2 ** n
if x >= nn:
    x = 0

ans = []

for i in range(n):
    oks = [True] * nn
    oks[x] = False
    cur = 0
    for j in ans[::-1]:
        cur ^= j
        oks[cur] = False
        oks[cur ^ x] = False
    try:
        a = next(j for j, ok in enumerate(oks[1:], 1) if ok)
    except StopIteration:
        break
    ans = [*ans, a, *ans]

print(len(ans))
if ans:
    print(' '.join(map(str, ans)))

