n = int(input())
A = [int(i) for i in input().split()]
ans = 0
curmax = 10**10
for i in range(n - 1, -1, -1):
    if curmax == 0:
        continue
    if A[i] < curmax:
        ans += A[i]
        curmax = A[i]
    else:
        ans += curmax - 1
        curmax -= 1
print(ans)
