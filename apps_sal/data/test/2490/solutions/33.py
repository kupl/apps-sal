def main():
    n = input()
    a, b = 0, 1
    for i in n:
        x = int(i)
        a, b = min(a + x, b + 10 - x), min(a + x + 1, b + 10 - x - 1)
    print(a)

main()

