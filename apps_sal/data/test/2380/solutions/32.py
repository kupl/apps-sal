from collections import deque
details = list(map(int, input().split()))
N = details[0]
M = details[1]
cards = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(M)]
ab = sorted(ab, key=lambda x: x[1], reverse=True)
cards = deque(sorted(cards))
counter = 0
for i in range(M):
    for j in range(ab[i][0]):
        if ab[i][1] > cards[0]:
            cards.popleft()
            cards.append(ab[i][1])
            counter += 1
            if counter == N:
                break
        else:
            break
    if counter == N:
        break
print(sum(cards))
