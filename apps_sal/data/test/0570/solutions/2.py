def main():
    (a, b) = list(map(int, input().split()))
    cur = 1
    while True:
        if a < cur:
            print('Vladik')
            break
        a -= cur
        if b < cur + 1:
            print('Valera')
            break
        b -= cur + 1
        cur += 2


try:
    while True:
        main()
except EOFError:
    pass
