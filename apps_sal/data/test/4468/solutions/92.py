(N, T) = list(map(int, input().split()))
tt = list(map(int, input().split()))
ans = 0
for i in range(N - 1):
    nn = tt[i + 1] - tt[i]
    if nn > T:
        ans += T
    else:
        ans += nn
ans += T
print(ans)
