n, t = [int(i) for i in input().split()]
list_route = [list(map(int, input().split())) for list_route in range(n)]
ans = 1001
for i in range(0, n):
    if list_route[i][1] <= t and ans >= list_route[i][0]:
        ans = list_route[i][0]
if ans != 1001: print(ans)
else: print("TLE")
