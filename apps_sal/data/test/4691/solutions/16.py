dic = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}
N = int(input())
for i in range(N):
    dic[input()] += 1
for i in dic:
    print(i, 'x', dic[i])
