from collections import defaultdict

n, m = map(int, input().split())
l = [int(x) for x in input().split()]

Dict, has, sum, ans = defaultdict(lambda: 0), False, 0, 0
Dict[0] = 1
for i in range(n):
    if l[i] > m:
        sum += 1
    elif l[i] < m:
        sum -= 1
    else:
        has = True

    if has:
        ans += Dict[sum] + Dict[sum - 1]
    else:
        Dict[sum] += 1
print(ans)
