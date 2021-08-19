n = int(input())
s = [input() for i in range(n)]
results = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}
for res in s:
    results[res] += 1
for (r, num) in results.items():
    print(f'{r} x {num}')
