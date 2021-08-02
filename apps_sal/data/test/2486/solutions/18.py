N, K = map(int, input().split())
A = [int(x) for x in input().split()]
A.sort(reverse=True)
su = 0
ans = 0
for a in A:
    if su + a < K:
        su += a
        ans += 1
    else:
        ans = 0
print(ans)
