def main():
    n, b, d = map(int, input().split())
    arr = list(map(int, input().split()))
    num = 0
    taken = 0
    for i in arr:
        if (i > b):
            continue
        taken += i

        if (taken > d):
            taken = 0
            num += 1
    print(num)


main()
