def ii():
    return int(input())


def ss():
    return [x for x in input()]


def si():
    return [int(x) for x in input().split()]


def mi():
    return map(int, input().split())


a, b = mi()
s = []
ans = 0
key = True

for i in range(a):
    i = si()
    s.append(i)
    ans += sum(i)

for i in range(a - 1):
    if not (s[i][0] < s[i + 1][0] and s[i][-1] < s[i + 1][-1]):
        ans = -1
        key = False
        break
for i in range(b - 1):
    if not (s[0][i] < s[0][i + 1] and s[-1][i] < s[-1][i + 1]):
        ans = -1
        key = False
        break

for i in range(a - 2, 0, -1):
    if not key:
        break
    for x in range(b - 2, 0, -1):
        if s[i][x] < s[i + 1][x] and s[i][x] < s[i][x + 1] and (min(s[i + 1][x], s[i][x + 1]) - max(s[i - 1][x], s[i][x - 1])) > 1:
            if s[i][x] == 0:
                s[i][x] = min(s[i + 1][x], s[i][x + 1]) - 1
                ans += s[i][x]
        else:
            ans = -1
            key = False
            break
print(ans)
