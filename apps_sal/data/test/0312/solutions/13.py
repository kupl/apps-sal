n, m = (int(i) for i in input().split())
def solve():
    if n == 1:
        return 1
    # For n > 1, at least one of [a1, a2] must be valid

    a1 = m - 1
    a2 = m + 1
    if a1 < 1:
        return a2
    
    if a2 > n:
        return a1

    b1 = a1 # Numbers from 1 to a1 inclusive
    b2 = n - a2 + 1 # Numbers from a2 to n inclusive
    return a1 if b1 >= b2 else a2
    # "If there are multiple such values, print the minimum of them."

print(solve())

