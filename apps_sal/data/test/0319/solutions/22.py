import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
lights = [[int(x) for x in input().strip()] for i in range(N)]

A = [sum([lights[i][j] for i in range(N)]) for j in range(M)]
full = [i for i, x in enumerate(A) if x > 1]


def main():
    for row in lights:
        if sum(row) == sum([row[i] for i in full]):
            return "YES"
    return "NO"


print(main())
