ls = list(map(int, input().split()))
r = ls[0]
d = ls[1]
n = int(input())
ans = 0
for i in range(n):
    l = list(map(int, input().split()))
    x = l[0]
    y = l[1]
    rd = l[2]
    ds = (abs(x) ** 2 + abs(y) ** 2) ** 0.5
    if ds - rd >= r - d and ds + rd <= r:
        ans += 1
print(ans)
