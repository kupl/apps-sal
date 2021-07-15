#!/usr/bin/env python3
# import bisect

n, k = list(map(int, input().split()))
x = list(map(int, input().split()))

# index = bisect.bisect(list, 0)

# left = index
# right = n - index

# if left != 0:
#     if x[index-1] == 0:
#         k -= 1
#         del(x[index-1])

ans = 10**9
for i in range(0, n-k+1):
    # print(x[i], x[i+k-1])
    if x[i]*x[i+k-1] >= 0:
        ans_tmp = max(abs(x[i]), abs(x[i+k-1]))
    else:
        ans_tmp = abs(x[i]) + abs(x[i+k-1]) + min(abs(x[i]), abs(x[i+k-1]))

    # print(ans_tmp)
    ans = min(ans, ans_tmp)
# print()
print(ans)

