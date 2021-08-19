import sys
sys.setrecursionlimit(10 ** 9)
(H, N) = map(int, input().split())
magic = [_ for _ in range(N)]
for k in range(N):
    magic[k] = list(map(int, input().split()))
    magic[k].append(magic[k][0] / magic[k][1])
magic.sort(key=lambda x: x[2], reverse=True)
ans = [0 for _ in range(H + 1)]
visited = [0]
anskouho = [float('inf')]


def solve(start, power, point, maryoku):
    if start == H:
        print(min(point, min(anskouho)))
        return
    elif start > H:
        anskouho.append(point)
        visited.sort(reverse=True)
        return 0
    elif ans[start] != 0:
        visited.sort(reverse=True)
        return 0
    else:
        visited.append(start)
        ans[start] = point
        solve(start + power, power, point + maryoku, maryoku)


for k in range(N):
    for item in visited:
        solve(item + magic[k][0], magic[k][0], ans[item] + magic[k][1], magic[k][1])
print(min(anskouho))
