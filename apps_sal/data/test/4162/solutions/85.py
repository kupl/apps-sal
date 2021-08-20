(N, *A) = map(int, open(0).read().split())
m = 1
ans = 0
for a in A:
    ans += a - 1
print(ans)
