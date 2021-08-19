n = int(input())
ta = [list(map(int, input().split())) for _ in range(n)]
(tv, av) = (1, 1)
for (t, a) in ta:
    i = (t + tv - 1) // t
    j = (a + av - 1) // a
    k = max(i, j)
    tv = t * k
    av = a * k
print(tv + av)
