import bisect
n = int(input())
A = list(map(int, input().split()))
A.sort()
if n == 2:
    ans = [A[1], A[0]]
    print(*ans)
    return
MAX = A[-1]
target = MAX // 2
ok = 0
ng = n
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if A[mid] <= target:
        ok = mid
    else:
        ng = mid
ans = [MAX, A[ok]]

nxt = ok + 1
# print(A[nxt])
if nxt < n:
    dif0 = min(MAX - A[ok], A[ok])
    dif1 = min(MAX - A[nxt], A[nxt])
    if dif0 < dif1:
        ans[1] = A[nxt]
print(*ans)
