N = int(input())
K = int(input())
A = list(map(int, input().split()))

ans = 0
for a in A:
    ans += 2 * min(a, K - a)
print(ans)
