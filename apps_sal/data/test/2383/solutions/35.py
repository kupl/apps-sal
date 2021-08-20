n = int(input())
a = list(map(int, input().split()))
(i, ans, j) = (1, 0, 0)
while j < n:
    if a[j] == i:
        i += 1
    else:
        ans += 1
    j += 1
if ans == n:
    print(-1)
else:
    print(ans)
