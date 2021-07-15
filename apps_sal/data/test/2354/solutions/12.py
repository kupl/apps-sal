import sys

def __starting_point():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    size = data[0]
    n = data[1]
    #size, n = map(int, input().split())
    plus = (size * size + size % 2) // 2
    for i in range(n):
        x, y = data[i * 2 + 2], data[i * 2 + 3]
        print(((x - 1) * size + y + 1) // 2 + (x + y) % 2 * plus)
__starting_point()
