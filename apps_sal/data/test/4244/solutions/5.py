n = int(input())
L = list(map(int, input().split()))
(l, r, ans) = (min(L), max(L), 10 ** 18)
for i in range(l, r + 1):
    total = 0
    for l in L:
        total += (l - i) ** 2
    ans = min(ans, total)
print(ans)
