import random


def genTemp():
    sl = ''
    firstTime = True
    while firstTime or sl in pre or sl in post:
        sl = ''
        firstTime = False
        for i in range(6):
            sl += chr(random.randint(ord('a'), ord('z')))
    return sl


n = int(input())
e = 0
pre = set()
post = set()
for i in range(n):
    (name, tp) = input().split()
    if tp == '1':
        e += 1
        pre.add(name)
    else:
        post.add(name)
temp = genTemp()
preAns = {str(x) for x in range(1, e + 1)}
postAns = {str(x) for x in range(e + 1, n + 1)}
preMissing = preAns - pre
postMissing = postAns - post
preToChange = pre - preAns
postToChange = post - postAns
preFree = preMissing - postToChange
postFree = postMissing - preToChange
preWrong = preToChange & postMissing
postWrong = postToChange & preMissing
ans = []
while preToChange or postToChange:
    if not postFree and (not preFree):
        if preToChange:
            x = preToChange.pop()
            preWrong.discard(x)
            ans.append(('move', x, temp))
            preToChange.add(temp)
            if x in postAns:
                postFree.add(x)
        else:
            x = postToChange.pop()
            ans.append(('move', x, temp))
            postWrong.discard(x)
            postToChange.add(temp)
            if x in postAns:
                preFree.add(x)
    elif preFree:
        if preWrong:
            x = preWrong.pop()
            preToChange.discard(x)
        else:
            x = preToChange.pop()
        y = preFree.pop()
        ans.append(('move', x, y))
        preMissing.discard(y)
        if x in postAns:
            postFree.add(x)
    else:
        if postWrong:
            x = postWrong.pop()
            postToChange.discard(x)
        else:
            x = postToChange.pop()
        y = postFree.pop()
        ans.append(('move', x, y))
        postMissing.discard(y)
        if x in preAns:
            preFree.add(x)
print(len(ans))
for tup in ans:
    print(*tup)
