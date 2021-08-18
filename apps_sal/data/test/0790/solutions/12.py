import sys

n, k = list(map(int, input().split(' ')))

activate = list(map(int, input().split(' ')))
deactivate = list(map(int, input().split(' ')))
ls = list(zip(activate[0:-1], deactivate[0:-1]))
diff = ls[0][0] - ls[0][1]

presum = [0 for _ in range(n + 2)]

for i in range(1, n + 1):
    presum[i] = presum[i - 1] + activate[i - 1]

ret = 0

if k == 0:
    for i in range(1, n + 1):
        ret = max(ret, presum[n] - presum[i - 1] - deactivate[i - 1])
elif k == 1:

    ret = max(ret, presum[n - 1] - min(deactivate), presum[n] - min(deactivate) - deactivate[n - 1])

    deac = sorted(deactivate[0:n - 1])
    ac = sorted(activate[1:n - 1])

    ret = max(ret, presum[n] - deactivate[0] - ac[0])
    ret = max(ret, presum[n] - deac[0] - deac[1])

    for i in range(2, n + 1):
        ret = max(ret, presum[n] - presum[i - 1] - deactivate[i - 1])
else:
    for i in range(1, n):
        ret = max(ret, presum[n] - deactivate[i - 1])

    ret = max(ret, activate[n - 1] - deactivate[n - 1])

print(ret)
