def counter(s, t):

    how_many = 0

    for i in range(0, len(s) - len(t) + 1):

        if s[i:i + len(t)] == t:
            how_many += 1

    return how_many


while True:

    inp = input().split()

    n = int(inp[0])
    k = int(inp[1])

    s = input()

    returning = s

    for i in range(1, n + 1):
        if counter(returning + s[-i:], s) > counter(returning, s):
            addition = s[-i:]
            break

    returning = s + (k - 1) * addition

    print(returning)

    break
