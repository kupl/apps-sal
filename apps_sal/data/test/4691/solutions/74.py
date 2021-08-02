n = int(input())
a = [input() for i in range(n)]

for i in ['AC', 'WA', 'TLE', 'RE']:
    print(f'{i} x {a.count(i)}')
