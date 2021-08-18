from sys import stdin


def readline(): return tuple(map(int, input().split()))


def bdiff(creature): return max(0, creature[0] - creature[1])


n, a, b = readline()
hand = [tuple(map(int, line.split())) for line in stdin.readlines()]

ans = sum(creature[1] for creature in hand)
if b:
    hand.sort(key=bdiff)

    best = 0
    if n > b:
        lost = bdiff(hand[n - b])
        for creature in hand[:n - b]:
            best = max(best, (creature[0] << a) - creature[1] - lost)

    for creature in hand[max(0, n - b):]:
        best = max(best, (creature[0] << a) - max(creature))
        ans += bdiff(creature)
    ans += best

print(ans)
