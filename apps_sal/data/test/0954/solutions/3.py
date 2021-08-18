
def main():
    try:
        while True:
            s = input()
            a = set()
            for i in range(len(s)):
                a.add(s)
                s = s[1:] + s[0]

            print(len(a))

    except EOFError:
        pass


main()
