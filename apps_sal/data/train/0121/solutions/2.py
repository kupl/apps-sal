def iinput():
    return [int(x) for x in input().split()]


def main():
    n = int(input())
    data = iinput()
    data.sort()
    return abs(data[n] - data[n - 1])


for t in range(int(input())):
    print(main())
