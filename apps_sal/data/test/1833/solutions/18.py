import math
from collections import defaultdict
n = int(input())
arr = list(map(int, input().strip().split()))
MOD = 1000000007
pre = defaultdict(int)


def get_divisors(k, upper):
    div = []
    for i in range(2, min(upper, int(math.floor(math.sqrt(k)))) + 1):
        if k % i == 0:
            div.append(i)
            if k // i <= upper:
                div.append(k // i)
    if k <= upper:
        div.append(k)
    return div


for i in range(n):
    div = get_divisors(arr[i], i + 1)
    update = {}
    for d in div:
        if pre[d - 1] == 0:
            continue
        update[d] = (pre[d] + pre[d - 1]) % MOD
    pre.update(update)
    pre[1] += 1
print(sum(pre.values()) % MOD)
