n, k = [int(a) for a in input().split()]
power = [int(a) for a in input().split()]
coins = [int(a) for a in input().split()]

dp = [0 for i in range(n)]


def takeSecond(elem):
    return elem[1]


def takeFirst(elem):
    return elem[0]


people = [(power[i], coins[i], i) for i in range(n)]

people.sort(key=takeFirst)

dp[0] = []

for i, p in enumerate(people):
    if i == 0:
        continue
    kills = [i for i in dp[i - 1]]
    kills.append(people[i - 1][1])
    x = []

    if len(kills) > k:
        kills.remove(min(kills))

    dp[i] = kills

x = [(people[i][2], str(sum(dp[i]) + people[i][1])) for i in range(n)]

x.sort(key=takeFirst)

print(" ".join([z[1] for z in x]))
