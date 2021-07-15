Rows, Columns = 0, 0
Spiders = []

def ReadInput():
    nonlocal Rows, Columns, Spiders
    Rows, Columns, spiderCount = map(int, input().split())
    Spiders = [0 for i in range(0, Columns)]
    for x in range(0, Rows):
        line = input()
        for y in range(0, Columns):
            if line[y] == 'L':
                if y - x >= 0:
                    Spiders[y - x] += 1
            elif line[y] == 'R':
                if y + x < Columns:
                    Spiders[y + x] += 1
            elif line[y] == 'U':
                if x % 2 == 0:
                    Spiders[y] += 1

def PrintOutput():
    nonlocal Rows, Columns, Spiders
    for y in range(0, Columns):
        print(Spiders[y], end = " ")
    print("\n")

def main():
    ReadInput()
    PrintOutput()

main()
