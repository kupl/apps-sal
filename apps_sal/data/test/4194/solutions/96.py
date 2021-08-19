(n, m) = map(int, input().split())
a_list = list(map(int, input().split()))
a_total = sum(a_list)
ans = n - a_total
if ans < 0:
    print(-1)
else:
    print(ans)
