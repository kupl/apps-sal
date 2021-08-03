N = int(input())
W = list(map(int, input().split()))
ans = 10**9
for i in range(1, N):
    if sum(W[:i]) >= sum(W[i:]):
        print(min(ans, abs(sum(W[:i]) - sum(W[i:]))))
        break

    ans = abs(sum(W[:i]) - sum(W[i:]))
