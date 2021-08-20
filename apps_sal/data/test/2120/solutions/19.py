(n, m) = list(map(int, input().split()))
fun = [int(x) for x in input().split()]
ans = 0
for i in range(m):
    (a, b) = list(map(int, input().split()))
    ans += min(fun[a - 1], fun[b - 1])
print(ans)
