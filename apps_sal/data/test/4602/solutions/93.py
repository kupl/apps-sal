N = int(input())
K = int(input())
X = list(map(int, input().split()))

ans = 0

for i in X:
    Y = []
    Y.append(2 * abs(i))
    Y.append(2 * abs(i - K))
    ans += min(Y)

print(ans)
