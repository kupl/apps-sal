from itertools import accumulate

n = int(input())
d = list(map(int, input().split()))

left = list(accumulate([0] + d))
right = list(accumulate([0] + d[::-1]))

ans = 0
i, j = 0, 0

while i + j <= n:
    le, ri = left[i], right[j]

    if le == ri:
        ans = le
        i += 1
        j += 1

    elif le < ri:
        i += 1

    elif le > ri:
        j += 1

    else:
        return

print(ans)
