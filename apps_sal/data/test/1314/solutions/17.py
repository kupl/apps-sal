from math import inf


def main():
    count = int(input())
    x = 0
    y = 0
    for a in range(count):
        arr = input().split()
        x += int(arr[0])
        y += int(arr[1])
        arr = input().split()
        x += int(arr[0])
        y += int(arr[1])
    x //= count
    y //= count
    print(x, y)


main()
