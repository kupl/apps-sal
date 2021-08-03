from collections import deque

details = list(map(int, input().split()))

N = details[0]
M = details[1]

cards = list(map(int, input().split()))

ab = [list(map(int, input().split())) for _ in range(M)]

ab = sorted(ab, key=lambda x: x[1], reverse=True)

cards = deque(sorted(cards, reverse=True))


for i in range(M):
    for j in range(ab[i][0]):
        if ab[i][1] > cards[-1]:
            cards.pop()
            cards.appendleft(ab[i][1])
        else:
            break

print(sum(cards))
