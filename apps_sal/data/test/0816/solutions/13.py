
def main():
    from collections import Counter

    try:
        while True:
            n, trg = list(map(int, input().split()))
            a = list(map(int, input().split()))
            c = Counter(a)
            result = 0
            for x in a:
                result += c[trg ^ x]
            if trg == 0:
                result -= n
            print(result >> 1)

    except EOFError:
        pass


main()
