(n, k) = list(map(int, input().strip().split()))
if k != 0:
    ans = [1 + k, 1]
else:
    ans = [1, 2]
i = 2
z = ans[1]
while i < 2 * n:
    z += 1
    if z == 1 + k:
        continue
    ans.append(z)
    i += 1
print(*ans)
