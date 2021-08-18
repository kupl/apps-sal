
import sys

N = int(input())
now = int(sys.stdin.readline().strip())
ans = [now]

for n in range(N - 1):
    now = int(sys.stdin.readline().strip())

    if now > ans[0]:
        ans[0] = now
    elif ans[-1] >= now:
        ans.append(now)
    else:
        left = 0
        right = len(ans) - 1

        while right - left > 1:
            mid = (right + left) // 2
            if now > ans[mid]:
                right = mid
            else:
                left = mid

        ans[right] = now

print((len(ans)))
