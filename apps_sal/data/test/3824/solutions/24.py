
def main():
    x0, y0 = list(map(int, input().split()))
    x1, y1 = list(map(int, input().split()))
    print((max(abs(x1 - x0), 1) + max(abs(y1 - y0), 1)) * 2 + 4)


try:
    while True:
        main()
except EOFError:
    pass
