def main():
    from collections import Counter
    try:
        while True:
            c = Counter(input())
            print(min(c['B'], c['u'] >> 1, c['l'], c['b'], c['a'] >> 1, c['s'], c['r']))
    except EOFError:
        pass


main()
