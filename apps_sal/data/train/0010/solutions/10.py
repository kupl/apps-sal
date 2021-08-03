def main():
    n = int(input())
    lst = list(map(int, input().split()))
    take = [lst[0]]
    sign = 0
    for i in range(1, n):
        if i == n - 1:
            take.append(lst[i])
        else:
            if lst[i] > take[-1]:
                if lst[i + 1] < lst[i]:
                    take.append(lst[i])
            elif lst[i] < take[-1]:
                if lst[i + 1] > lst[i]:
                    take.append(lst[i])
    line = str(len(take)) + '\n'
    for i in take:
        line += str(i) + ' '
    print(line)


def __starting_point():
    t = int(input())
    for i in range(t):
        main()


__starting_point()
