from sys import stdin
import re

def readInt(count=1):
    m = re.match('\s*' + ('([+-]?\d+)\s*' * count), stdin.readline())
    if m is not None:
        ret = []
        for i in range(1, m.lastindex + 1):
            ret.append(int(m.group(i)))
        return ret
    return None

taskCount, = readInt()
thinkingTime = readInt(taskCount)
onlineCount, = readInt()
online = []
for i in range(onlineCount):
    online.append(readInt(2))

totalThinking = sum(thinkingTime)
best = -1
for i in range(onlineCount):
    if online[i][0] >= totalThinking:
        if best == -1 or online[i][0] < best:
            best = online[i][0]
    elif online[i][1] >= totalThinking:
        best = totalThinking
        break
print(best)

