(n, k) = list(map(int, input().split()))
arr = [int(i) for i in input().split()]
ans = [0] * 2001
for i in arr:
    ans[i] += 1
r = 0
j = 2000
while j >= 0:
    z = k
    m = 0
    while z > 0 and j > 0:
        if ans[j] >= z:
            m = max(m, j)
            ans[j] -= z
            z = 0
            break
        z -= ans[j]
        if ans[j] > 0:
            m = max(j, m)
        ans[j] = 0
        j -= 1
    if ans[j] == 0:
        j -= 1
    if m > 1:
        r += 2 * (m - 1)
print(r)
