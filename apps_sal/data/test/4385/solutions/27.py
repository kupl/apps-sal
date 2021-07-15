def Input():
    return mapt(int, input().split(" "))


def calc(i, h):
    return all(h[i] >= h[j] for j in range(i))


def main():
    data = [int(input()) for _ in range(5)]
    k = int(input())
    print("Yay!" if k >= data[-1] - data[0] else ":(")


main()
