N, K = list(map(int, input().split()))
x = [int(p) for p in input().split()]
x.sort()
x = x[::-1]
pp = 0
ans = 0
for a in x:
    if pp + a < K:
        pp += a
        ans += 1
    else:
        ans = 0
print(ans)
