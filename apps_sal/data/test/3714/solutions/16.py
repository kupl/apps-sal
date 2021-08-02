def make_function(n, crushes):
    def f(original_node):
        node = original_node
        x = 0
        for i in range(n):
            node = crushes[node]
            x += 1
            if node == original_node:
                break
        else:
            return -1
        return x / 2 if x % 2 == 0 else x
    return f


def lcd(numbers):
    gcd = lambda x, y: int(x) if y == 0 else int(gcd(y, x % y))
    ret = 1
    for number in numbers:
        ret = ret * number / gcd(ret, number)
    return ret


def main():
    n = int(input())
    a = list(map(int, input().split()))
    crushes = {i: x for i, x in zip(list(range(1, n + 1)), a)}
    f = make_function(n, crushes)
    numbers = list(map(int, list(map(f, crushes))))
    if -1 in numbers:
        print(-1)
        return
    print(int(lcd(numbers)))


main()
