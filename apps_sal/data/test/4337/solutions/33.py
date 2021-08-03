def decision(pack: list) -> str:
    if "Y" in pack:
        return "Four"
    return "Three"


def __starting_point():
    n = int(input())
    pack = list(map(str, input().split()))
    print(decision(pack))


__starting_point()
