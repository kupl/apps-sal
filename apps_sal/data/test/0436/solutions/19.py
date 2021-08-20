n = int(input())
a = list(map(int, input().split()))
m = a[0]
ans = [1]
s = m + 0
all_s = sum(a)
for i in range(1, n):
    if 2 * a[i] <= m:
        ans.append(i + 1)
        s += a[i]
if 2 * s > all_s:
    print(len(ans))
    print(*ans)
else:
    print(0)
