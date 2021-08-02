def check(v, length, start, target):
    n = len(v)
    end_x = start[0] + int(length / n) * v[-1][0]
    end_y = start[1] + int(length / n) * v[-1][1]

    if length % n != 0:
        end_x += v[length % n - 1][0]
        end_y += v[length % n - 1][1]

    if abs(target[0] - end_x) + abs(target[1] - end_y) <= length:
        return True
    return False


start = list(map(int, input().split()))  # [0, 7]
end = list(map(int, input().split()))  # [103080, -3000000]
n = int(input())
seed = input()  # 'LUDRUDRL'

v = []
dx = {'R': 1, 'L': -1, 'U': 0, 'D': 0}
dy = {'R': 0, 'L': 0, 'U': 1, 'D': -1}

cur = [0, 0]
for c in seed:
    cur = [cur[0] + dx[c], cur[1] + dy[c]]
    v.append(cur)
# print(v)

inf = 1 << 64
l = 0
u = inf

while(u - l > 1):
    md = int((l + u) / 2)
    if check(v, md, start, end):
        u = md
    else:
        l = md

if u != inf:
    print(u)
else:
    print(-1)
