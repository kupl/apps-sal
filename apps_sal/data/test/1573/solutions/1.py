(n, d) = list(map(int, input().split()))
v = []
for i in range(0, n):
    (a, b) = list(map(int, input().split()))
    v.append((a, b))
v = sorted(v)
lo = 0
totalFriendship = v[0][1]
bestFriendship = totalFriendship
for i in range(1, n):
    while v[i][0] - v[lo][0] >= d:
        totalFriendship -= v[lo][1]
        lo += 1
    totalFriendship += v[i][1]
    bestFriendship = max(bestFriendship, totalFriendship)
print(bestFriendship)
