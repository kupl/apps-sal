q = int(input())
n = 10**5
nums = [False] * 2 + [True] * (n - 2)
ans = [0] * n
for i in range(2, n):
    if nums[i]:
        for j in range(i * 2, n, i):
            nums[j] = False
pre = 0
for i in range(3, n, 2):
    if nums[i] and nums[(i + 1) // 2]:
        ans[i] += pre + 1
        pre = ans[i]
    else:
        ans[i] = pre
for _ in range(q):
    l, r = list(map(int, input().split()))
    print((ans[r] - ans[max(l - 2, 1)]))
