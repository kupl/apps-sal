from itertools import combinations
(n, m, x) = map(int, input().split())
ca = [list(map(int, input().split())) for _ in range(n)]
ans = float('inf')
for i in range(1, n + 1):
    for i1 in combinations(ca, i):
        nums = [0] * (m + 1)
        for i2 in i1:
            for i3 in range(m + 1):
                nums[i3] += i2[i3]
        if min(nums[1:]) >= x:
            if nums[0] < ans:
                ans = nums[0]
if ans == float('inf'):
    print(-1)
else:
    print(ans)
