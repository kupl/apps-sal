def main():
    y, b, r = map(int, input().split())
    mn = min(r - 2, b - 1, y)
    if (mn < 0):
        print(0)
    else:
        print(mn * 3 + 3)

main()
