import math

N, K = [int(x) for x in input().split()]

res = 0
sum = 0

arr = [int(x) for x in input().split()]
arrK = [int(x) - 1 for x in input().split()]

for i in range(0, N):
    res += arr[i] * arr[i - 1]
    sum += arr[i]

dictU = {}
used = 0
for i in arrK:
    cur = i
    if cur == 0:
        pre = N - 1
    else:
        pre = cur - 1
    if cur == N - 1:
        next = 0
    else:
        next = cur + 1
    tmp = 0
    if pre in dictU:
        tmp += arr[pre]
    if next in dictU:
        tmp += arr[next]

    test = arr[cur] * (sum - arr[cur] - arr[pre] - arr[next] - used + tmp)
    res += test
    dictU[cur] = True
    used += arr[cur]

print(res)
