def iroha():
    lists = [input() for _ in range(2)]
    reversed_text = ''.join(list(reversed(lists[0])))
    print(("YES" if reversed_text == lists[1] else "NO"))

def __starting_point():
    iroha()


__starting_point()
