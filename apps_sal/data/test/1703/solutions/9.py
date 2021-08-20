from collections import Counter


def read():
    return int(input())


def readlist():
    return list(map(int, input().split()))


def readmap():
    return map(int, input().split())


N = read()
S_list = []
for _ in range(N):
    S_list.append(input())
LEFT = []
RIGHT = []
both = 0
for i in range(N):
    S = S_list[i]
    left_usable = True
    right_usable = True
    left = 0
    right = 0
    for s in S:
        if s == '(':
            left += 1
        else:
            right += 1
            if left < right:
                left_usable = False
                break
    if left_usable:
        leftnum = left - right
    left = 0
    right = 0
    for s in reversed(S):
        if s == ')':
            right += 1
        else:
            left += 1
            if left > right:
                right_usable = False
                break
    if right_usable:
        rightnum = -left + right
    if left_usable and right_usable:
        both += 1
    elif left_usable:
        LEFT.append(leftnum)
    elif right_usable:
        RIGHT.append(rightnum)
ans = 0
LEFT.sort()
RIGHT.sort()
counter_left = Counter(LEFT)
counter_right = Counter(RIGHT)
ans += both ** 2
le = []
for (k, v) in counter_left.items():
    le.append((k, v))
ri = []
for (k, v) in counter_right.items():
    ri.append((k, v))
i = 0
j = 0
while i < len(le) and j < len(ri):
    if le[i][0] == ri[j][0]:
        ans += le[i][1] * ri[j][1]
        i += 1
        j += 1
    elif le[i][0] < ri[j][0]:
        i += 1
    else:
        j += 1
print(ans)
