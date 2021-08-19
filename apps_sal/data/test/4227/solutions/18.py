import itertools
(N, M) = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(M)]
lst = [x for x in range(2, N + 1)]
l = itertools.permutations(lst)
ans = 0
for num in l:
    t = [1] + list(num)
    ok = True
    for j in range(N - 1):
        p = sorted([t[j], t[j + 1]])
        if not p in s:
            ok = False
            break
    if ok:
        ans += 1
print(ans)
