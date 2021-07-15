n = int(input())
bs = list(map(int, input().split()))

def solve(n, bs):
    steps = 0
    level = 0
    for b in bs:
        steps += abs(level - b)
        level = b
    return steps

print(solve(n, bs))

