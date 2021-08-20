(N, K) = [int(x) for x in input().split()]
l = [int(x) for x in input().split()]
s = sorted(l)
ans = sum(s[N - K:])
print(ans)
