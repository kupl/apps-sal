n, m, k = list(map(int, input().split()))
s = list(map(int, input().split()))
sh = list(map(int, input().split()))
izb = list(map(int, input().split()))
ssh = {}
for i in range(n):
    if sh[i] not in ssh:
        ssh[sh[i]] = s[i]
    else:
        ssh[sh[i]] = max(ssh[sh[i]], s[i])
u = 0
result = 0
izb = sorted(izb)
for i in range(n):
    if u == len(izb):
        break
    if i + 1 == izb[u]:
        if ssh[sh[i]] > s[i]:
            result += 1
        u += 1
print(result)

