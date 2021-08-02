n = int(input())
d = {
    'AC': 0,
    'WA': 0,
    'TLE': 0,
    'RE': 0
}

for i in range(n):
    d[input()] += 1

for k, v in d.items():
    print(k, 'x', v)
