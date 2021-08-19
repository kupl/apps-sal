def main():
    try:
        while True:
            n = int(input())
            ls = []
            if n & 1:
                ls.append('3')
                n -= 3
            while n:
                ls.append('2')
                n -= 2
            print(len(ls))
            print(' '.join(ls))
    except EOFError:
        pass


main()
