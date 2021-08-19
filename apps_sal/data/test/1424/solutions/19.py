def byte_v(a, n):
    ans = []
    while a != 0:
        ans.append(a % 2)
        a //= 2
    ans.reverse()
    ans = (n - len(ans)) * [0] + ans
    return ans


(n, m, k) = map(int, input().split())
players = []
for i in range(m + 1):
    curr_army = int(input())
    players.append(list(byte_v(curr_army, n)))
phill = players[-1]
ans = 0
for i in range(m):
    curr = 0
    for j in range(n):
        if phill[j] != players[i][j]:
            curr += 1
    if curr <= k:
        ans += 1
print(ans)
