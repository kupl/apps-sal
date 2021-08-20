n = int(input())
a = list([1 if int(x) > 0 else -1 for x in input().split()])
(last, pr) = (0, 1)
for q in a:
    pr *= q
    if pr > 0:
        last += 1
ans = last
for q in range(1, len(a)):
    if a[q - 1] > 0:
        last -= 1
    else:
        last = n - q - last
    ans += last
print(n * (n + 1) // 2 - ans, ans)
