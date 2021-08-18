import operator
import bisect

n = int(input())
red = [tuple(map(int, input().split())) for _ in range(n)]
blue = [tuple(map(int, input().split())) for _ in range(n)]

red.sort(key=operator.itemgetter(0, 1))
blue.sort(key=operator.itemgetter(0, 1))
count = 0
for i in range(n):
    for j in reversed(list(range(len(red)))):
        if not red:
            break
        if red[j][0] < blue[i][0]:
            tmp = red[:j + 1]
            tmp.sort(key=lambda x: x[1], reverse=True)
            for t in tmp:
                if t[1] < blue[i][1]:
                    count += 1
                    red.pop(red.index(t))
                    break
        else:
            continue
        break

print(count)
