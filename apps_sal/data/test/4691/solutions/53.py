import collections
N = int(input())
j = [input() for i in range(N)]
c = collections.Counter(j)
cs = c['AC']
ca = c['WA']
cb = c['TLE']
cc = c['RE']
print(f'AC x {cs}')
print(f'WA x {ca}')
print(f'TLE x {cb}')
print(f'RE x {cc}')
