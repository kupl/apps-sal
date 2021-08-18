n = int(input())
dlist = list(map(int, input().split()))

dlist_sorted = sorted(dlist)

kiwa_upper = dlist_sorted[n // 2]
kiwa_low = dlist_sorted[(n // 2) - 1]

if len(dlist_sorted[n // 2:]) != n // 2:
    print(0)
else:
    print(kiwa_upper - kiwa_low)
