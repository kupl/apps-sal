N = int(input())
cnt = {}
for _ in range(N):
    s = ''.join(sorted(input(), key=str.lower))
    if s in cnt:
        cnt[s] += 1
    else:
        cnt[s] = 1
res = 0
for val in cnt.values():
    res += val * (val - 1) // 2
print(res)
