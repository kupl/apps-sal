import collections
dic = collections.defaultdict(int)

n, m = map(int, input().split())
p = list(map(int, input().split()))

sum = 0
flag = False
dic[0] = 1
ans = 0
for v in p:
    if v < m:
        sum -= 1
    elif v > m:
        sum += 1

    if v == m:
        flag = True

    if flag:
        ans += dic[sum] + dic[sum - 1]
    else:
        dic[sum] += 1

print(ans)
