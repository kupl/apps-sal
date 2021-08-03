def main():
    for _ in range(int(input())):
        a, b = map(int, input().split())
        x = len(str(b))
        if b == int('9' * x):
            x += 1
        print(a * (x - 1))


main()
