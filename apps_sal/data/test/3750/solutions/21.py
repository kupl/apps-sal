(k, a, b) = map(int, input().split())
ans = a // k + b // k
if ans == 0 or (min(a, b) < k and max(a, b) % k):
    print(-1)
else:
    print(ans)
