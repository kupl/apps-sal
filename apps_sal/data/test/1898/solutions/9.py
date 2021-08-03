
def main():
    n = int(input())
    result = ["hate", "love"] * ((n + 1) // 2)
    result = result[:n]
    print("I " + " that I ".join(result) + " it")


def __starting_point():
    main()


__starting_point()
