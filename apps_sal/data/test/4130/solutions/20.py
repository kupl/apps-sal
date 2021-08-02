N = int(input())
A = sorted([int(a) for a in input().split()])

k = 0
ans = 0
for i in range(N):
    if k > A[i]:
        pass
    elif k >= A[i] - 1:
        ans += 1
        k += 1
    else:
        ans += 1
        k = A[i] - 1
print(ans)
