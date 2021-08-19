n = int(input())
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))

s = list(input())
x, y = list(map(int, input().split()))

it = [0, 0, 0, 0]

for i in range(len(s)):
    if s[i] == 'U':
        s[i] = 0
    elif s[i] == 'R':
        s[i] = 1
    elif s[i] == 'D':
        s[i] = 2
    else:
        s[i] = 3
    it[s[i]] += 1


def distance(x, y, xx, yy):
    return abs(x - xx) + abs(y - yy)


def yes(steps, ost, x, y):
    xx = steps[1] - steps[3]
    yy = steps[0] - steps[2]
    return distance(x, y, xx, yy) <= ost


ans = 0


if distance(x, y, 0, 0) > n or (x + y + n) % 2 == 1:
    print(-1)
elif yes(it, 0, x, y):
    print(0)
else:
    i = -1
    cur_ans = 0
    max_ans = 0

    steps = [0, 0, 0, 0]

    while yes(steps, n - cur_ans, x, y):
        i += 1
        steps[s[i]] += 1
        cur_ans += 1

    steps[s[i]] -= 1
    i -= 1
    cur_ans -= 1
    max_ans = cur_ans

    j = n
    ok = True

    while j > 0 and ok:
        j = j - 1
        steps[s[j]] += 1
        cur_ans += 1

        while i >= 0 and not yes(steps, n - cur_ans, x, y):
            steps[s[i]] -= 1
            i -= 1
            cur_ans -= 1

        if yes(steps, n - cur_ans, x, y) and cur_ans > max_ans:
            max_ans = cur_ans
        ok = (i >= 0) or yes(steps, n - cur_ans, x, y)

    print(n - max_ans)
