from sys import stdin
inFile = stdin
tokens = []
tokens_next = 0

def next_str():
    nonlocal tokens, tokens_next
    while tokens_next >= len(tokens):
        tokens = inFile.readline().split()
        tokens_next = 0
    tokens_next += 1
    return tokens[tokens_next - 1]

def nextInt():
    return int(next_str())

def check(a, n):
    # a must be sorted in decresing order
    if n == 0:
        return 0
    if len(a) <= n:
        return 1
    l = [[i] for i in a[:n]]
    allowed = [i for i in a[:n]]
    ind = 0
    for i in a[n:]:
        ind += 1
        ind %= len(allowed)
        starting_pos = ind
        while allowed[ind] == 0:
            ind += 1
            ind %= len(l)
            if ind == starting_pos:
#                 print(l, 0)
                return 0
        l[ind] += [i]
        allowed[ind] = min(i, allowed[ind] - 1)
#     print(l, 1)
    return 1

def solve(a):
    a.sort(reverse=1)
    n = len(a)
    low = 0
    high = n
    while low + 1 < high:
        m = (low + high) // 2
        if check(a, m):
            high =  m
        else :
            low = m
    return high

n = nextInt()
a = [nextInt() for i in range(n)]

print(solve(a))




