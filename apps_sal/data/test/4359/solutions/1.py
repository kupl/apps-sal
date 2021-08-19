from itertools import permutations


def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(' '))


def calc(i, h):
    return all((h[i] >= h[j] for j in range(i)))


def main():
    ans = 1000
    data = [int(input()) for i in range(5)]
    for row in permutations(data, 5):
        time = 0
        for (index, i) in enumerate(row):
            if index == 4:
                time += i
                continue
            remain = i % 10
            if remain:
                time += i + (10 - remain)
            else:
                time += i
        ans = min(ans, time)
    print(ans)


main()
