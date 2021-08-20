import math
n = int(input())
B = list(map(int, input().split()))


def solve(B):
    odds = []
    evens = []
    for b in B:
        if b % 2 == 0:
            evens.append(b)
        else:
            odds.append(b)
    if len(evens) == 0:
        return []
    even_gcd = evens[0]
    for e in evens:
        even_gcd = math.gcd(even_gcd, e)
    even_remove = [even_gcd * x for x in solve([e // even_gcd for e in evens])]
    if len(odds) + len(even_remove) < len(evens):
        return odds + even_remove
    else:
        return evens


ans = solve(B)
print(len(ans))
if len(ans) != 0:
    print(' '.join([str(x) for x in ans]))
