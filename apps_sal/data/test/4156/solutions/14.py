n, w = list(map(int, input().split()))
arr = list(map(int, input().split()))
mx = 0
mn = 0
curr = 0
for i in arr:
    curr += i
    mx = max(curr, mx)
    mn = min(curr, mn)
ans = w + 1 - (mx - mn)
if ans < 0:
    print(0)
else:
    print(ans)
