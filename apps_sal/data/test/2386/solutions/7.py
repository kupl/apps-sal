import statistics
import math
N = int(input())
A_list = list(map(int, input().split()))
A_list_min = 10 ** 9 + 1
A_list_sum = 0
for i in range(N):
    A_list[i] = A_list[i] - (i + 1)
A_medi = int(statistics.median(A_list))
ans = 0
for i in range(N):
    ans += abs(A_list[i] - A_medi)
print(ans)
