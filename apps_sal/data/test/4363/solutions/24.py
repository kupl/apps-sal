def answer(k: int, s: int) -> int:
    count = 0
    
    for x in range(k + 1):
        y_max = min(k, s - x)
        y_min = max(0, s - x - k)
        comb = y_max - y_min + 1
        
        if 0 < comb:
            count += comb

    return count


def main():
    k, s = map(int, input().split())
    print(answer(k, s))


def __starting_point():
    main()
__starting_point()
