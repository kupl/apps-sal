n = int(input())
ar = list(map(int, input().split()))
x = ar[0]
ans = [1]
s = sum(ar)
s2 = x
for i in range(1, n):
    if 2 * ar[i] <= x:
        ans.append(i + 1)
        s2 += ar[i]
if 2 * s2 > s:
    print(len(ans))
    print(*ans)
else:
    print(0)
