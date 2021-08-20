(n, m) = list(map(int, input().split()))
arr = [int(x) for x in input().split()]
d = [0] * n
ans = 0
for i in range(m):
    (a, b) = list(map(int, input().split()))
    s = 0
    for j in range(a - 1, b):
        s += arr[j]
    if s > 0:
        ans += s
print(ans)
