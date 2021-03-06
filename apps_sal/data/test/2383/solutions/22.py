import sys
input = sys.stdin.readline


def main2():
    numbers = []
    N = int(input())
    numbers = list(map(int, input().split()))
    n = 1
    for x in numbers:
        if x == n:
            n += 1
    answer = N - n + 1
    if answer == N:
        answer = -1
    print(answer)


def main():
    numbers = []
    n = int(input())
    numbers = list(map(int, input().split()))
    buffer = [0]
    for i in range(1, n + 1):
        search_range = numbers[i - 1:]
        out_range = len(numbers[:i - 1])
        if i not in search_range and len(buffer) == 1:
            print(-1)
            return
        elif i not in search_range or i == n:
            break
        else:
            index = search_range.index(i)
            buffer.append(index - sum(buffer))
    print(sum(buffer))


def __starting_point():
    main2()


__starting_point()
