def max_index(a: list) -> int:
    return a.index(max(a))


def main():
    n = int(input())
    a = list(map(int, input().split()))
    alice_number = 0
    bob_number = 0
    while len(a) > 0:
        alice_number += a.pop(max_index(a))
        if len(a) == 0:
            break
        else:
            bob_number += a.pop(max_index(a))
    print((alice_number - bob_number))


def __starting_point():
    main()


__starting_point()
