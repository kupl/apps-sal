

n, k = list(map(int, input().split()))


scorelist = list(map(int, input().split()))


keylist = list(input())


keystreaks = []


currentstreak = [[scorelist[0], keylist[0]]]


for i in range(1, n):
    if keylist[i] == keylist[i - 1]:
        currentstreak.append([scorelist[i], keylist[i]])

    else:
        keystreaks.append(currentstreak)
        currentstreak = [[scorelist[i], keylist[i]]]


keystreaks.append(currentstreak)


bigtotal = 0

for streak in keystreaks:
    total = 0
    streak.sort(key=lambda x: -x[0])
    tally = 0
    while tally < k and tally < len(streak):
        total = total + streak[tally][0]
        tally += 1
    bigtotal = bigtotal + total


print(bigtotal)
