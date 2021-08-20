import math
N = int(input())
result = [10 ** 13]
cnt = []
for i in range(1, int(math.sqrt(N)) + 1):
    if N % i == 0:
        buf = min(result[-1], i + N // i)
        result.append(buf)
        if result[-1] != result[-2]:
            cnt.append([i, N // i])
print(cnt[-1][0] - 1 + cnt[-1][1] - 1)
