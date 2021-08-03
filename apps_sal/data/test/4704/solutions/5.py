N = int(input())
a = [int(x) for x in input().split()]
ans = 10**9 * N
front = 0
back = sum(a)
for i in range(N - 1):
    front += a[i]
    back -= a[i]
    ans = min(ans, abs(front - back))
print(ans)
