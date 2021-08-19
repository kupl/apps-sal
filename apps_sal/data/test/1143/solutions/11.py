"""input
2
5 23 1 2
3 13 2 3
"""
from sys import stdin, stdout


def get_time(m, d, t):
    month = ['dum', 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0
    for i in range(1, m):
        day += month[i]
    day += d
    end = day
    start = end - t
    return (start, end)


stdin = open('input.txt', 'r')
stdout = open('output.txt', 'w')
n = int(stdin.readline().strip())
time_line = []
for _ in range(n):
    (m, d, p, t) = list(map(int, stdin.readline().split()))
    (start, end) = get_time(m, d, t)
    time_line.append([start, p])
    time_line.append([end, -p])
time_line = sorted(time_line, key=lambda x: (x[0], x[1]))
ans = 0
temp = 0
for i in range(len(time_line)):
    temp += time_line[i][1]
    ans = max(ans, temp)
stdout.write(str(ans))
