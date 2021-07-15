n, k = map(int, input().split())


def count(s):
    return min(s-1, 2*n + 1 - s)

ans = 0
for i in range(2, 2*n+1):
    if 2<=i-k<=2*n:
        ans += count(i)*count(i-k)

print(ans)
