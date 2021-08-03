n = int(input())
d = [int(x.strip()) for x in input().split()]
d_sorted = sorted(d)
m = int(n / 2)
abc_fin = d_sorted[m - 1]
arc_start = d_sorted[m]
if abc_fin == arc_start:
    ans = 0
else:
    ans = arc_start - abc_fin
print(ans)
