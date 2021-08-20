import sys
X = int(sys.stdin.readline())
a = set([int(i) for i in sys.stdin.readline().split()])
top = 1 << 31
ans = 0


def best(s, cur):
    if len(s) == 0 or cur == 0:
        return 0
    hasCur = set()
    hasNotCur = set()
    for i in s:
        if i & cur == 0:
            hasNotCur.add(i)
        else:
            hasCur.add(i)
    if len(hasNotCur) == 0 or len(hasCur) == 0:
        return best(s, cur >> 1)
    else:
        return cur + min(best(hasNotCur, cur >> 1), best(hasCur, cur >> 1))


print(best(a, top))
