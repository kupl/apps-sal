def resolve():
    """
    code here
    """
    N = int(input())
    As = [int(item) for item in input().split()]
    box = set()
    for i in range(N):
        num = N - i
        sum_num = 0
        for j in range(1, N // num + 1):
            if j * num in box:
                sum_num += 1
        if As[num - 1] != sum_num % 2:
            box.add(num)
    print(len(box))
    for item in box:
        print(item)


def __starting_point():
    resolve()


__starting_point()
