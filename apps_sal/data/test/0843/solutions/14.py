def main():
    n = int(input())
    arrows = input()
    cells = [int(x) for x in input().split()]
    print(solver(arrows, cells))


def solver(arrows, cells):
    for i in range(len(arrows)):
        if arrows[i] == '<':
            cells[i] = - cells[i]
    visited = [False] * len(cells)
    index = 0
    while True:
        if index >= len(cells) or index < 0:
            return "FINITE"
        elif visited[index] == True:
            return "INFINITE"
        else:
            visited[index] = True
            index = index + cells[index]


main()
