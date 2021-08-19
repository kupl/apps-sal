# alpha = "abcdefghijklmnopqrstuvwxyz"
# prime = 998244353
# INF = 1000_000_000

# from heapq import heappush, heappop
# from collections import defaultdict
# from math import sqrt
# from collections import deque
# from math import gcd

n = int(input())
arr = list(map(int, input().split()))
ans = arr[0]
ans_arr = [1]
ind = 2
for i in arr[1:]:
    if arr[0] >= 2 * i:
        ans_arr.append(ind)
        ans += i
    ind += 1
sum_ans = sum(arr)
if ans > sum_ans // 2:
    print(len(ans_arr))
    print(*ans_arr)
else:
    print(0)
