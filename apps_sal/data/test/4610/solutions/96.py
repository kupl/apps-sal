from collections import Counter


def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    n, k = Input()
    a = sorted(Counter(Input()).items(), key=lambda x:x[1], reverse=True)
    temp = 0
    for i in range(min(k, len(a))):
        temp += a[i][1]
    print(sum(i for _, i in a) - temp)


main()
