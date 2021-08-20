count = int(input())
lists = []
for i in range(count):
    new = input()
    lists.append(new)
ac_count = lists.count('AC')
wa_count = lists.count('WA')
tle_count = lists.count('TLE')
re_count = lists.count('RE')
print('AC x ' + str(ac_count))
print('WA x ' + str(wa_count))
print('TLE x ' + str(tle_count))
print('RE x ' + str(re_count))
