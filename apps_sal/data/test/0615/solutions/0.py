from bisect import bisect_right, bisect_left
n = int(input())
a = list(map(int, input().split()))
tmp = 0
ca = [0]
for ai in a:
    tmp += ai
    ca.append(tmp)
ans = float('inf')

f, g = 1, 3
for i in range(2, n - 1):
    while abs(ca[i] - ca[f] - ca[f]) > abs(ca[i] - ca[f + 1] - ca[f + 1]):
        f += 1
    while abs((ca[-1] - ca[g]) - (ca[g] - ca[i])) > abs((ca[-1] - ca[g + 1]) - (ca[g + 1] - ca[i])):
        g += 1
    l = (ca[f], ca[i] - ca[f], ca[-1] - ca[g], ca[g] - ca[i])
    ans = min(ans, max(l) - min(l))
print(ans)
