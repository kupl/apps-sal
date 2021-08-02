import sys

# D - Megalomania
N = int(input())
jobs = []

for _ in range(N):
    a, b = map(int, input().split())
    jobs.append([a, b])

# 締め切り時刻の順にソート
jobs.sort(key=lambda x: x[1])

time = 0

for i in range(N):
    time += jobs[i][0]

    if time > jobs[i][1]:
        print('No')
        return

print('Yes')
