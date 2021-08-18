import sys


def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    odds = sum([x % 2 for x in a])
    evens = n - odds
    if n == k:
        return "Daenerys" if odds % 2 == 0 else "Stannis"
    moves = n - k
    if moves % 2 == 0:
        eachmove = moves // 2
        if evens <= eachmove:
            remodds = k
            if remodds % 2 == 1:
                return "Stannis"
        return "Daenerys"
    else:
        dmoves = moves // 2
        if odds <= dmoves or (evens <= dmoves and (n - moves) % 2 == 0):
            return "Daenerys"
        return "Stannis"


if sys.hexversion == 50594544:
    sys.stdin = open("test.txt")
print(solve())
