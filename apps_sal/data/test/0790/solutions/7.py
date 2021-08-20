import sys
(n, k) = list(map(int, input().split(' ')))
activate = list(map(int, input().split(' ')))
deactivate = list(map(int, input().split(' ')))
presum = [0 for _ in range(n + 2)]
for i in range(1, n + 1):
    presum[i] = presum[i - 1] + activate[i - 1]
ret = 0
if k == 0:
    for i in range(1, n + 1):
        ret = max(ret, presum[n] - presum[i - 1] - deactivate[i - 1])
elif k == 1:
    for i in range(1, n):
        ret = max(ret, presum[n - 1] - deactivate[i - 1])
    if deactivate[n - 1] < activate[n - 1]:
        ret += activate[n - 1] - deactivate[n - 1]
    deac = sorted(deactivate[1:n - 1])
    ac = sorted(activate[1:n - 1])
    ret = max(ret, presum[n] - deac[0] - deac[1])
    ret = max(ret, presum[n] - deactivate[0] - ac[0])
    ret = max(ret, presum[n] - deactivate[0] - deac[0])
    for i in range(2, n + 1):
        ret = max(ret, presum[n] - presum[i - 1] - deactivate[i - 1])
else:
    for i in range(1, n):
        ret = max(ret, presum[n] - deactivate[i - 1])
    ret = max(ret, activate[n - 1] - deactivate[n - 1])
print(ret)
