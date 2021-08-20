def sum(n):
    r = 0
    while n:
        (r, n) = (r + n % 10, n // 10)
    return r


k = int(input())
ans = []
x = 0
for i in range(1, 10800101, 9):
    t = sum(i)
    if t == 10:
        if x == k:
            break
        ans.append(str(i))
        x += 1
print(ans[k - 1])
