N = int(input())
A = list(map(int, input().split()))
ans = 0
l = 0
r = N - 1
while True:
    if A[l] != A[r]:
        ans = r - l
        break
    l += 1
(l, r) = (0, N - 1)
while True:
    if A[l] != A[r]:
        ans = max(ans, r - l)
        break
    r -= 1
print(ans)
