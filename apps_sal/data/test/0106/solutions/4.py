from math import *
n, m, k = list(map(int, input().split()))
a, b = list(map(int, input().split()))
pod_a = ceil(a / (m * k))
pod_b = ceil(b / (m * k))
aa = a % (m * k)
if aa == 0:
    aa = m * k
bb = b % (m * k)
if bb == 0:
    bb = m * k
et_a = ceil(aa / k)
et_b = ceil(bb / k)
#print(pod_a, pod_b)
#print(et_a, et_b)
cnt = 0
if pod_a != pod_b:
    cnt += min(5 * (et_a - 1), 10 + et_a - 1)
    # print(cnt)
    et_a = 1
    if pod_a > pod_b:
        pod_b, pod_a = pod_a, pod_b
    cnt += min(pod_b - pod_a, n - (pod_b - pod_a)) * 15
    # print(cnt)
cnt += min(5 * abs(et_a - et_b), 10 + abs(et_a - et_b))
print(cnt)
