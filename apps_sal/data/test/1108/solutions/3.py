n = int(input())
ans = 0
for i in range(n):
    (p, q) = list(map(int, input().split()))
    ans += q - p >= 2
print(ans)
