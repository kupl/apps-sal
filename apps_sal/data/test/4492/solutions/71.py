N, x, *A = list(map(int, open(0).read().split()))
ans = 0
for i in range(1, N):
    required = (A[i] + A[i - 1]) - x
    if required <= 0:
        continue
    elif required <= A[i]:
        A[i] -= required
    else:
        A[i] = 0
        rem = required - A[i]
        A[i - 1] -= rem
    ans += required

print(ans)
