n = int(input())
a = list(map(int, input().split()))
INF = 10 ** 9

def how_many_times_divisible(x):
    ans = 0
    while x % 2 == 0:
        x /= 2
        ans += 1
    return ans

ans = INF
for i in range(n):
    if how_many_times_divisible(a[i]) < ans:
        ans = how_many_times_divisible(a[i])
print(ans)

