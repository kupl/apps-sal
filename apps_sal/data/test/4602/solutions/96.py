N = int(input())
K = int(input())
X = [int(x) for x in input().split()]

ans = 0
for x in X:
    ans += min(x, abs(x-K))
ans *= 2
print(ans)
