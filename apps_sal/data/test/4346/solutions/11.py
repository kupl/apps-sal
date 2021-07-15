n = int(input())
for q in range(n):
    L, v, l, r = list(map(int, input().split()))
    ac = L // v
    lc = l // v + (0 if l % v == 0 else 1)
    rc = r // v
    print(ac - (rc - lc + 1))

