(n, m) = list(map(int, input().split()))
N = list(map(int, input().split()))
M = list(map(int, input().split()))
N.sort()
M.sort()
a = N[-1]
ans = -1
for i in range(a, M[0]):
    if i >= 2 * N[0]:
        ans = i
        break
print(ans)
