__author__ = 'Krishna'

team_count = 0
jun, sen = (int(i) for i in input().split(" "))
mini = min(jun, sen)
maxi = max(jun, sen)
diff = maxi - mini
if diff < maxi and diff < mini:
    mini -= diff
    maxi -= 2 * diff
    team_count += diff
    team_count += 2 * (mini // 3)
    if mini % 3 == 2:
        team_count += 1
    print(team_count)
else:
    print(mini)
