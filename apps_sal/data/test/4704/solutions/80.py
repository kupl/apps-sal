n = int(input())
a = list(map(int, input().split()))
rui = []
rui.append(a[0])
for x in range(1, n):
    b = rui[-1] + a[x]
    rui.append(b)
ans = []
for y in range(n - 1):
    ans.append(abs(rui[n - 1] - rui[y] - rui[y]))
print(min(ans))
