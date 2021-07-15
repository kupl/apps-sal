T = int(input())

def solve(x, y):
    if x >= 4:
        return "YES"
    if x in [2, 3]:
        if y <= 3:
            return "YES"
    if x == 1:
        if y == 1:
            return "YES"
    return "NO"

for case in range(T):
    x, y = list(map(int, input().split()))
    print(solve(x, y))
