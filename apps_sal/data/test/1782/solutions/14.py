
n, k = map(int, input().split())
if n // k < 3:
    print("-1")
    return
ans = list()
for i in range(n):
    if i < 2 * k:
        ans.append(i // 2 + 1)
    elif (i // k) % 2 == 0:
        ans.append(i % k + 1)
    else:
        ans.append(k - i % k)
print(*ans)
