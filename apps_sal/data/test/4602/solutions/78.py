N = int(input())
K = int(input())
x = list(map(int, input().split()))

ans = 0

for x in x:
    a = 2 * x
    b = abs(K - x) * 2
    ans += min(a, b)

print(ans)
