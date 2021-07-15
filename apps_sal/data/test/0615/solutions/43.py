from itertools import accumulate
from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
s = list(accumulate(a))

ans = float("inf")

for j in range(2,n-1):
    i_list = []
    i_left = bisect_left(s, s[j-1]//2)-1
    if i_left != -1:
        i_list.append([s[i_left], s[j-1]-s[i_left]])
    if i_left != j-2:
        i_list.append([s[i_left+1], s[j-1]-s[i_left+1]])

    k_list = []
    k_left = bisect_left(s, s[j-1]+(s[-1]-s[j-1])//2)-1
    if k_left != j-1:
        k_list.append([s[k_left] - s[j-1], s[-1]-s[k_left]])
    if k_left != n-2:
        k_list.append([s[k_left+1] - s[j-1], s[-1]-s[k_left+1]])
    for i in i_list:
        for k in k_list:
            tmp = max(i+k)-min(i+k)
            ans = min(ans, tmp)
print(ans)
