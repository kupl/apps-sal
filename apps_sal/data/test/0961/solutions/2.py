people = int(input())
cities = list(map(int, input().split()))
maximum = max(cities)
(last, first) = ([-1 for i in range(maximum + 1)], [float('inf') for i in range(maximum + 1)])
for i in range(people):
    first[cities[i]] = min(i, first[cities[i]])
    last[cities[i]] = max(i, last[cities[i]])
dp = [0 for i in range(people)]
dp[0] = cities[0] if last[cities[0]] == 0 else 0
for i in range(1, people):
    min_first = float('inf')
    max_last = -1
    used = set()
    xor = 0
    for j in range(i, -1, -1):
        min_first = min(min_first, first[cities[j]])
        max_last = max(max_last, last[cities[j]])
        if cities[j] not in used:
            xor ^= cities[j]
        used.add(cities[j])
        if min_first >= j and max_last <= i:
            if j != 0:
                dp[i] = max(dp[i], dp[j - 1] + xor)
            else:
                dp[i] = max(dp[i], xor)
    dp[i] = max(dp[i], dp[i - 1])
print(dp[-1])
