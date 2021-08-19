def getHeight(s: str) -> int:
    h = maxh = 0
    for c in s:
        h += 1 if c == '[' else -1
        maxh = max(h, maxh)
    return maxh


def makeColumn(height: int, maximumHeight: int) -> str:
    half = (maximumHeight - height) * [' '] + ['+'] + height * ['|']
    return half + half[-2::-1]


(n, s) = (int(input()), input())
h = getHeight(s)
ans = [makeColumn(h, h)]
curh = h - 1
for i in range(1, n):
    if s[i] == ']':
        if s[i - 1] == '[':
            for j in range(3):
                ans.append([' '] * (h * 2 + 1))
        curh += 1
        ans.append(makeColumn(curh, h))
    else:
        ans.append(makeColumn(curh, h))
        curh -= 1
for line in zip(*ans):
    for i in range(len(line)):
        if (i > 0 and line[i - 1] == '+' or (i < len(line) - 1 and line[i + 1] == '+')) and line[i] == ' ':
            print('-', end='')
        else:
            print(line[i], end='')
    print()
