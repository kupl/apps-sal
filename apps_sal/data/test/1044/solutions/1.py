try:
    while True:
        n = int(input())
        prev = 0
        for x in map(int, input().split()):
            prev = prev + x - 1 & 1
            print('21'[prev])
except EOFError:
    pass
