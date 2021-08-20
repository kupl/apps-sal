import collections


def solve(sets):
    n = len(sets)
    sets.sort(key=lambda x: x[0])
    (s, f) = (sets[0][0], sets[0][1])
    ans = 1
    for i in range(1, n):
        if sets[i][0] <= f:
            s = max(s, sets[i][0])
            f = min(f, sets[i][1])
        else:
            ans += 1
            s = sets[i][0]
            f = sets[i][1]
    return ans


n = int(input().strip())
sets = []
for i in range(n):
    sets.append(list(map(int, input().strip().split())))
print(solve(sets))
