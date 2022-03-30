n, k = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]
diff = [x[i] - x[i - 1] for i in range(1, n)]
if len(list([x for x in diff if x > k])) > 0:
    print(-1)
    return
ans = 1
cur = 0
for i in diff:
    if cur + i > k:
        ans += 1
        cur = i
    else:
        cur += i
print(ans)
