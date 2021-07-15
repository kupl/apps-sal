import bisect

n, q = [int(v) for v in input().split()]
va = [int(v) for v in input().split()]
vk = [int(v) for v in input().split()]

for i in range(1, n):
    va[i] += va[i - 1]

ans = []
curr = 0
for k in vk:
    curr += k
    it = bisect.bisect_right(va, curr)
    if it == n:
        ans.append(n)
        curr = 0
    else:
        ans.append(n - it)

print('\n'.join(str(v) for v in ans))

