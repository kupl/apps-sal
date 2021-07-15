Cards = {'a':list(input()),'b':list(input()),'c':list(input())}

def solve(p):
    nonlocal Cards
    if len(Cards[p]) == 0:
        return p.capitalize()
    np = Cards[p].pop(0)
    return solve(np)

print(solve('a'))
