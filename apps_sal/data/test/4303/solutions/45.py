import sys
n, k = list(map(int, input().split()))
x_ls = list(map(int, input().split()))
x_ls.sort()
if x_ls[0] >= 0:
    print((x_ls[k - 1]))
    return
elif x_ls[-1] <= 0:
    x_ls.sort(reverse=True)
    print((abs(x_ls[k - 1])))
    return
l = 0
r = k - 1
ans = float('inf')
while r < n:
    cost_1 = 2 * abs(x_ls[l]) + abs(x_ls[r])
    cost_2 = abs(x_ls[l]) + 2 * abs(x_ls[r])
    cost = min(cost_1, cost_2)
    ans = min(cost, ans)
    r += 1
    l += 1
print(ans)
