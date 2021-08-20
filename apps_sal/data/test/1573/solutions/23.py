(n, d) = map(int, input().split())
friends = [(0, 0)]
for i in range(n):
    (money, cute) = map(int, input().split())
    friends.append((money, cute))
friends.sort()
sumcute = [0 for i in range(n + 1)]
for i in range(1, n + 1):
    sumcute[i] = sumcute[i - 1] + friends[i][1]
l = 1
r = 1
ans = 0
while r != len(sumcute):
    while r != len(sumcute) - 1 and friends[r + 1][0] - friends[l][0] < d:
        r += 1
    ans = max(sumcute[r] - sumcute[l - 1], ans)
    if r == len(sumcute) - 1:
        r += 1
    l += 1
print(ans)
