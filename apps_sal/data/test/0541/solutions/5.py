from operator import itemgetter
N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]

ab.sort(key=itemgetter(1))
ans = [0]
for a, b in ab:
    if ans[-1] < a:
        ans.append(b - 1)
print(len(ans) - 1)
