n = int(input())
segments = [list(map(int, (input() + " " + str(i + 1)).split())) for i in range(n)]
ssegments = sorted(segments, key=lambda seg: seg[1], reverse=True)
ssegments = sorted(ssegments, key=lambda seg: seg[0])

good = True
for s in ssegments:
    if ssegments[0][0] > s[0] or ssegments[0][1] < s[1]:
        good = False
        break

if good:
    print(ssegments[0][2])
else:
    print(-1)
