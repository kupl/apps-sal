n = int(input())
k = list(map(int, input().split()))
ans = 10 ** 9
for i in range(n):
    m = list(map(int, input().split()))
    ans = min(ans, 15 * len(m) + 5 * sum(m))
print(ans)
