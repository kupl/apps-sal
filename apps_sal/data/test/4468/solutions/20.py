(N, T) = map(int, input().split())
t_List = [int(x) for x in input().split()]
pre = 0
ans = T
for t in t_List:
    if t - pre <= T:
        ans += t - pre
    else:
        ans += T
    pre = t
print(ans)
