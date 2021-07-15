# python3
from sys import stdin

def main():
    def parseints(line): return tuple(map(int, line.split()))
    def bdiff(creature): return max(0, creature[0] - creature[1])

    n, a, b = parseints(input())
    hand = list(map(parseints, stdin.readlines()))

    ans = sum(creature[1] for creature in hand)  # default damage
    if b:
        hand.sort(key=bdiff)

        best = 0
        if n > b:
            lost = bdiff(hand[n - b])
            for creature in hand[:n-b]:
                best = max(best, (creature[0] << a) - creature[1] - lost)

        for creature in hand[max(0,n-b):]:
            best = max(best, (creature[0] << a) - max(creature))
            ans += bdiff(creature)
        ans += best

    print(ans)


main()

