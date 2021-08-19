from bisect import bisect_right
N = int(input())
A = [int(input()) for _ in range(N)]
A = A[::-1]
LIS = []
for ai in A:
    index = bisect_right(LIS, ai)
    if index >= len(LIS):
        LIS.append(ai)
    else:
        LIS[index] = ai
print(len(LIS))
