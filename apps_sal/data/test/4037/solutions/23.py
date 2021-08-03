def myFunc(e):
    return e[0] + e[1]


count, rating = list(map(int, input().split()))
goodJob = []
badJob = []

taken = 0

for i in range(count):
    a, b = list(map(int, input().split()))
    if b >= 0:
        goodJob.append([a, b])
    else:
        badJob.append([a, b])

goodJob.sort()
badJob.sort(reverse=True, key=myFunc)

for job in goodJob:
    if job[0] <= rating:
        rating += job[1]
        taken += 1
    else:
        break

dp = []

for i in range(len(badJob) + 1):
    row = []
    for j in range(rating + 2):
        row.append(0)
    dp.append(row)

dp[0][rating] = taken

for i in range(len(badJob)):
    for curRating in range(rating + 1):
        if curRating >= badJob[i][0] and curRating + badJob[i][1] >= 0:
            dp[i + 1][curRating + badJob[i][1]] = max(dp[i + 1][curRating + badJob[i][1]], dp[i][curRating] + 1)
        dp[i + 1][curRating] = max(dp[i + 1][curRating], dp[i][curRating])

ans = 0

for curRating in range(rating + 1):
    ans = max(ans, dp[len(badJob)][curRating])

print(ans)
