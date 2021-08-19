import heapq


def digitJump(text):
    L = len(text)

    if L == 1 or L == 2:
        return L - 1

    numPos = [[] for i in range(10)]
    minJump = [2000000 for _ in range(L)]
    minJump[L - 1] = 0

    maxJumpForNum = [2000000 for _ in range(10)]

    for i in range(L):
        numPos[int(text[i])].append(i)

    h = []
    heapq.heappush(h, (0, int(text[L - 1]), L - 1))

    while len(h) > 0:
        minJ, num, idx = heapq.heappop(h)
        setJump = minJ + 1

        # print(f"minJ: {minJ}  num: {num}  idx: {idx}")

        if maxJumpForNum[num] > setJump:
            maxJumpForNum[num] = setJump

            for i in numPos[num]:
                if i == idx:
                    continue
                if minJump[i] > setJump:
                    minJump[i] = setJump
                    heapq.heappush(h, (setJump, num, i))

        if idx > 0:
            if minJump[idx - 1] > setJump:
                minJump[idx - 1] = setJump
                heapq.heappush(h, (setJump, int(text[idx - 1]), idx - 1))

        if idx < L - 2:
            if minJump[idx + 1] > setJump:
                minJump[idx + 1] = setJump
                heapq.heappush(h, (setJump, int(text[idx + 1]), idx + 1))

    return minJump[0]


def __starting_point():
    text = input().strip()
    print(digitJump(text))


__starting_point()
