N = int(input())
S_list = [input() for i in range(N)]
ac = S_list.count('AC')
wa = S_list.count('WA')
tle = S_list.count('TLE')
re = S_list.count('RE')
print(f'AC x {ac}')
print(f'WA x {wa}')
print(f'TLE x {tle}')
print(f'RE x {re}')
