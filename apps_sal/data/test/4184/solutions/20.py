n = int(input())
w = list(map(int, input().split()))

ans = 10**9
for x in range(n - 1):
    s1 = sum(w[:x + 1])
    s2 = sum(w[x + 1:])
    if abs(s1 - s2) < ans:
        ans = abs(s1 - s2)

print(ans)
