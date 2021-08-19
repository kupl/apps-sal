(N, M) = map(int, input().split())
A = list(map(int, input().split()))
tab_sum = [0]
sum_tmp = 0
for Ai in A:
    sum_tmp += Ai
    tab_sum.append(sum_tmp)
cnt = {}
for item in tab_sum:
    key = str(item % M)
    cnt.setdefault(key, 0)
    cnt[key] += 1
ans = 0
for (key, val) in cnt.items():
    ans += val * (val - 1) // 2
print(ans)
